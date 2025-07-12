# Smart Research Assistant

## Project Overview

This AI-powered assistant is designed to help users deeply understand complex documents like research papers, technical manuals, or legal files by providing:

- **Comprehension-based Q&A**: Answering free-form questions grounded in the uploaded document.
- **Logic-based quizzes**: Generating reasoning questions and evaluating user responses with justifications.
- **Concise summarization**: Automatically generating a summary of no more than 150 words.
- **Document-aware interaction**: Ensuring all answers and evaluations are strictly based on the uploaded content with no hallucination.

The tool supports PDF and TXT document uploads and offers an intuitive web interface for seamless interaction.

---

## Functional Features

1. **Document Upload**
   - Upload PDF or TXT documents.
   - Supports structured English documents such as research papers or reports.

2. **Interaction Modes**
   - **Ask Anything**: Free-form question answering with contextual understanding based on the document.
   - **Challenge Me**: Generates 3 logic/comprehension questions; evaluates answers and provides feedback with justifications linked to the document.

3. **Contextual Understanding & Justification**
   - All responses are strictly grounded in the uploaded document content.
   - Every answer includes a reference or explanation pointing to the supporting section/paragraph.
   - The system avoids hallucinations or fabricated information.

4. **Auto Summary**
   - Generates a concise summary (≤ 150 words) immediately after document upload.

---

## Architecture & Reasoning Flow

- **Frontend**: Built using Streamlit for a clean and responsive user interface.
- **Document Processing**: PyMuPDF extracts text from PDFs; TXT files read natively.
- **NLP & AI**:
  - Hugging Face Transformers and SentenceTransformers power semantic understanding and similarity scoring.
  - Logic-based question generation derives reasoning-focused questions from the document.
  - Semantic similarity and rule-based evaluation mechanisms assess user answers.
- **Backend**: Core logic implemented in Python; the system is designed to run locally with modular components for easy expansion.
- **Memory & Context Handling** (Optional): Supports follow-up questions maintaining prior context.
- **Answer Highlighting** (Optional): Highlights exact document snippets supporting answers.

---

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/smart-research-assistant.git
cd smart-research-assistant
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open your browser at the indicated localhost URL to use the assistant.

Evaluation Criteria Alignment
Response Quality & Justification: Answers are generated with high accuracy and direct references to the document.

Reasoning Mode Functionality: The “Challenge Me” mode tests logic and comprehension with automatic evaluation.

UI/UX: Clean and intuitive interface with easy navigation and smooth workflow.

Code Quality: Well-structured and documented Python codebase.

Creativity & Bonus Features: Optional support for memory/context and answer highlighting enhances user experience.

Minimal Hallucination: Strict grounding in the source document content ensures factual correctness.

Contribution
Contributions and improvements are welcome. Please open issues or submit pull requests.

License
MIT License
