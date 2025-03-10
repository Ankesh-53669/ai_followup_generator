# AI Follow-Up Generator

## Overview
The AI Follow-Up Generator is a Flask-based web application that analyzes user-AI conversations and generates relevant follow-up questions. It helps improve dialogue coherence by identifying missing details or areas needing clarification.

## Features
- **Context Analysis**: Identifies gaps and missing details in AI responses.
- **Follow-Up Suggestions**: Generates 2-3 follow-up questions to refine the conversation.
- **Web Interface**: User-friendly UI to enter prompts and view suggestions.
- **Azure OpenAI Integration**: Uses Azure OpenAI's GPT-4 for analysis and suggestion generation.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **AI Model**: Azure OpenAI GPT-4

---

## Installation & Setup

### 1. Clone the Repository
```bash
git https://github.com/Ankesh-53669/ai-followup-generator.git
cd ai-followup-generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Set up your Azure OpenAI credentials:
```bash
export AZURE_OPENAI_ENDPOINT="your_endpoint"
export AZURE_OPENAI_KEY="your_api_key"
```

On Windows create .env file in src folder add the below keys:

AZURE_OPENAI_ENDPOINT="your_endpoint"
AZURE_OPENAI_KEY="your_api_key"
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Web Interface
Open your browser and visit:
```
http://127.0.0.1:5000/
```

---

## Usage Instructions
1. Enter a **User Prompt** and an **AI Response** in the form fields.
2. Click **Generate Follow-ups**.
3. View 2-3 suggested follow-up questions.

---

## Project Structure
:```
ai-followup-generator/
│── src/
│   ├── static/
│   │   └── style.css           # CSS for styling the UI
│   ├── templates/
│   │   └── index.html          # HTML frontend
│   ├── app.py                  # Flask backend
│   ├── .gitignore              # Git ignore file
│   ├── requirements.txt        # Dependencies
│── README.md                   # Documentation
```

---

## API Reference
### `/` (GET & POST)
**Method:** `POST`
- **Inputs:**
  - `user_prompt`: The user's original message.
  - `ai_response`: The AI-generated response.
- **Outputs:**
  - `followups`: List of suggested follow-up questions.

---

## Assumptions & Limitations
- The model relies on Azure OpenAI GPT-4, which may have response variability.
- UI is minimalistic for demonstration purposes.
- Additional refinements (e.g., NLP pre-processing) could enhance accuracy.

---

## Future Enhancements
- **Multimodal Support**: Voice input and response analysis.
- **Fine-Tuned Suggestions**: Better ranking of follow-up questions.
- **User Feedback Mechanism**: Allow rating of generated follow-ups.

---

## Contribution Guidelines
Feel free to fork the repo and submit pull requests!

---

## Contact & Support
For queries, reach out to:
- Email: ankesh.pandey@techenhance.com
- GitHub Issues: [GitHub Repo Issues](https://github.com/Ankesh-53669/ai-followup-generator/issues)

---

## License
MIT License. Free to use and modify.

