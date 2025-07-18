
# Smart Research Assistant

## Project Overview

This AI-powered assistant is designed to help users deeply understand complex documents such as research papers, technical manuals, or legal files by providing:

- Comprehensive, context-aware answers to free-form questions based on the uploaded document.
- Logic-based question generation to challenge users’ comprehension and reasoning.
- Automatic evaluation of user responses with detailed feedback and justifications grounded in the source document.
- A concise summary (≤ 150 words) generated immediately upon document upload.

The system supports PDF and TXT document uploads and offers an intuitive web-based interface for smooth, responsive interaction.

### Demo Video



https://github.com/user-attachments/assets/6818c98c-0c50-4aae-8c3a-04f29b5e11d1



---

## Functional Requirements

1. **Document Upload**
   - Accepts PDF or TXT documents.
   - Assumes structured English reports, research papers, or similar.

2. **Auto Summary**
   - Generates a concise summary (≤ 150 words) immediately after upload.
  
     <img width="2877" height="941" alt="image" src="https://github.com/user-attachments/assets/d8b2a03e-be23-4307-b7db-38ef50b80e9d" />

3. **Interaction Modes**
   - **Ask Anything**: Users ask free-form questions; assistant provides answers grounded in the document.
   - **Challenge Me**: Assistant generates three logic-based/comprehension questions; users submit answers; assistant evaluates responses and provides feedback with document-based justifications.

     <img width="2100" height="1177" alt="image" src="https://github.com/user-attachments/assets/98eb68d0-9ad8-4e87-8be9-2a2169b659f3" />


4. **Contextual Understanding**
   - All answers and evaluations strictly based on the uploaded document content.
   - No hallucinations or fabricated information.
   - Each response includes references (e.g., “Supported by paragraph 3 of section 1”).

   <img width="2862" height="1471" alt="image" src="https://github.com/user-attachments/assets/35fac5a5-c7fe-486a-b579-838747faf40d" />



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

