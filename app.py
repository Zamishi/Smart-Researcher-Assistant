# Enhanced Smart Research Assistant with Improved UI & Export Feature
import streamlit as st
import fitz  # PyMuPDF
import re
import spacy
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# --- Setup ---
st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("📚 Smart Research Assistant")

# --- Load models ---
@st.cache_resource(show_spinner=False)
def load_summarizer():
    return pipeline("summarization", model="t5-small", tokenizer="t5-small")

@st.cache_resource(show_spinner=False)
def load_qa_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_resource(show_spinner=False)
def load_direct_qa():
    return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

@st.cache_resource(show_spinner=False)
def load_spacy_model():
    return spacy.load("en_core_web_sm")

summarizer = load_summarizer()
qa_model = load_qa_model()
qa_model_direct = load_direct_qa()
nlp = load_spacy_model()

# --- Text extraction ---
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_txt(txt_file):
    return txt_file.read().decode("utf-8")

# --- Text chunking ---
def chunk_text(text, max_chunk_len=500, min_chunk_len=40):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) < max_chunk_len:
            chunk += sentence + " "
        else:
            if len(chunk.strip()) >= min_chunk_len:
                chunks.append(chunk.strip())
            chunk = sentence + " "
    if chunk.strip():
        chunks.append(chunk.strip())
    return chunks

# --- Improved question generation ---
def generate_questions_from_summary(summary_text):
    doc = nlp(summary_text)
    questions = []

    for sent in doc.sents:
        np_chunks = [chunk.text for chunk in sent.noun_chunks if len(chunk.text.split()) <= 5]
        for np in np_chunks:
            if "system" in np.lower() or "method" in np.lower() or "approach" in np.lower():
                q = f"What does the {np.strip()} aim to do?"
                questions.append((q, sent.text.strip()))
            elif "problem" in np.lower() or "challenge" in np.lower():
                q = f"What challenge is highlighted in '{np.strip()}'?"
                questions.append((q, sent.text.strip()))
            elif "technique" in np.lower() or "model" in np.lower():
                q = f"How is {np.strip()} used in the context?"
                questions.append((q, sent.text.strip()))
            elif np.lower() in ["fraud", "data", "performance"]:
                q = f"What is said about {np.strip()}?"
                questions.append((q, sent.text.strip()))
            elif len(np.strip()) > 3:
                q = f"What does the summary mention about {np.strip()}?"
                questions.append((q, sent.text.strip()))
            if len(questions) >= 5:
                break
        if len(questions) >= 5:
            break

    if not questions:
        questions.append(("What is the main point of the summary?", summary_text.strip()))

    return questions[:5]

# --- Semantic similarity scoring ---
def evaluate_answer(user_answer, correct_answer):
    embeddings = qa_model.encode([user_answer, correct_answer], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
    return similarity

# --- File Upload ---
with st.sidebar:
    st.header("📂 Upload Your Document")
    uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])

text = ""
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        text = extract_text_from_txt(uploaded_file)
    else:
        st.error("Unsupported file type!")

    if text.strip() == "":
        st.warning("Could not extract any text from the document.")
    else:
        st.success("✅ File uploaded and text extracted!")
        with st.expander("📖 View Extracted Text"):
            st.write(text[:3000] + "..." if len(text) > 3000 else text)

        with st.spinner("🔎 Generating summary..."):
            summary_text = summarizer(text[:2000], max_new_tokens=150, min_length=50, do_sample=False)[0]['summary_text']

        st.subheader("📝 Auto Summary (≤150 Words)")
        st.write(summary_text)

        mode = st.radio("🧭 Select Mode:", ["Ask Anything", "Challenge Me"])

        paragraphs = chunk_text(text)

        if mode == "Ask Anything":
            st.subheader("💬 Ask Anything from the Document")
            question = st.text_input("Type your question here:")
            if question:
                with st.spinner("🔍 Finding answer..."):
                    para_embeddings = qa_model.encode(paragraphs, convert_to_tensor=True)
                    question_embedding = qa_model.encode(question, convert_to_tensor=True)
                    similarities = util.cos_sim(question_embedding, para_embeddings)[0]
                    best_idx = similarities.argmax().item()
                    best_para = paragraphs[best_idx]
                    context_for_qa = text if len(text) < 4000 else best_para
                    result = qa_model_direct(question=question, context=context_for_qa)

                st.markdown(f"**Answer:** {result['answer']}")
                st.caption(f"Confidence: {round(result['score'] * 100, 2)}%")
                st.markdown("**Justification (source paragraph):**")
                st.info(best_para[:500] + "..." if len(best_para) > 500 else best_para)

        elif mode == "Challenge Me":
            st.subheader("🧠 Challenge Mode: Answer the Questions")
            if "challenge_questions" not in st.session_state:
                st.session_state.challenge_questions = generate_questions_from_summary(summary_text)
                st.session_state.challenge_answers = [ans for _, ans in st.session_state.challenge_questions]
                st.session_state.user_answers = [""] * len(st.session_state.challenge_questions)
                st.session_state.current_question = 0
                st.session_state.feedbacks = [""] * len(st.session_state.challenge_questions)

            idx = st.session_state.current_question
            q, correct_answer = st.session_state.challenge_questions[idx]
            st.write(f"**Q{idx+1}:** {q}")
            user_answer = st.text_area("Your Answer:", value=st.session_state.user_answers[idx], key=f"answer_{idx}")

            if st.button("Submit Answer"):
                sim = evaluate_answer(user_answer, correct_answer)
                st.session_state.user_answers[idx] = user_answer

                if sim > 0.75:
                    feedback = f"✅ Correct! (Similarity: {sim:.2f})"
                elif sim > 0.4:
                    feedback = f"⚠️ Partial match. (Similarity: {sim:.2f})"
                else:
                    feedback = f"❌ Not quite right. (Similarity: {sim:.2f})"

                st.session_state.feedbacks[idx] = feedback
                st.progress(min(sim, 1.0))

            if st.session_state.feedbacks[idx]:
                st.markdown(f"**Feedback:** {st.session_state.feedbacks[idx]}")
                st.markdown("**Justification (reference text):**")
                st.info(correct_answer[:500] + "..." if len(correct_answer) > 500 else correct_answer)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if st.button("⬅️ Previous") and idx > 0:
                    st.session_state.current_question -= 1
            with col3:
                if st.button("Next ➡️") and idx < len(st.session_state.challenge_questions) - 1:
                    st.session_state.current_question += 1

            # --- Export Report ---
            if st.button("📥 Download My Challenge Report"):
                report_lines = []
                for i, (q, correct) in enumerate(st.session_state.challenge_questions):
                    user = st.session_state.user_answers[i]
                    feedback = st.session_state.feedbacks[i]
                    report_lines.append(f"Q{i+1}: {q}\nYour Answer: {user}\nFeedback: {feedback}\nReference: {correct}\n{'-'*50}")
                report_txt = "\n".join(report_lines)
                st.download_button("Click to Download Report", report_txt, file_name="challenge_report.txt")
