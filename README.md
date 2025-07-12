
# Smart Research Assistant

## Project Overview

This AI-powered assistant is designed to help users deeply understand complex documents such as research papers, technical manuals, or legal files by providing:

- Comprehensive, context-aware answers to free-form questions based on the uploaded document.
- Logic-based question generation to challenge users’ comprehension and reasoning.
- Automatic evaluation of user responses with detailed feedback and justifications grounded in the source document.
- A concise summary (≤ 150 words) generated immediately upon document upload.

The system supports PDF and TXT document uploads and offers an intuitive web-based interface for smooth, responsive interaction.

---

## Functional Requirements

1. **Document Upload**
   - Accepts PDF or TXT documents.
   - Assumes structured English reports, research papers, or similar.

2. **Interaction Modes**
   - **Ask Anything**: Users ask free-form questions; assistant provides answers grounded in the document.
   - **Challenge Me**: Assistant generates three logic-based/comprehension questions; users submit answers; assistant evaluates responses and provides feedback with document-based justifications.

3. **Contextual Understanding**
   - All answers and evaluations strictly based on the uploaded document content.
   - No hallucinations or fabricated information.
   - Each response includes references (e.g., “Supported by paragraph 3 of section 1”).

4. **Auto Summary**
   - Generates a concise summary (≤ 150 words) immediately after upload.

---

## Architecture & Implementation

- **Frontend:** Streamlit-based web interface for easy document upload and user interaction.
- **Document Processing:** Uses PyMuPDF for PDF extraction; native reading for TXT files.
- **NLP & AI Components:**
  - Hugging Face Transformers and SentenceTransformers enable semantic understanding, question generation, and answer evaluation.
  - Logic-based questions generated dynamically from document content.
  - Semantic similarity and rule-based methods assess user answers.
- **Backend:** Core logic implemented in Python; designed for local execution with modular, maintainable code.
- **Bonus Features (Optional):**
  - Memory handling to maintain context for follow-up questions.
  - Answer highlighting to display document snippets supporting responses.

---

## Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Zamishi/Smart-Researcher-Assistant.git
cd smart-research-assistant
````

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
streamlit run app.py
```

5. **Open the provided localhost URL in your browser to start using the assistant.**

---

## Evaluation Criteria Alignment

* **Response Quality & Justification:** Accurate answers supported by explicit references to the document.
* **Reasoning Mode Functionality:** Robust “Challenge Me” mode generating meaningful logic questions with automatic answer evaluation.
* **UI/UX & Smooth Flow:** Clean, intuitive interface ensuring a seamless user experience.
* **Code Quality & Documentation:** Well-structured, readable, and thoroughly documented codebase with clear setup instructions.
* **Creativity & Bonus Features:** Optional memory and answer highlighting features enhance usability.
* **Minimal Hallucination & Good Context Use:** Strict grounding of all responses in source document to avoid fabrications.

---

## Contribution

Contributions, suggestions, and improvements are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.

