# LLM Article Question Answering

This is a simple Streamlit app that allows users to submit article URLs, process them, and then ask questions based on the content of those articles. The app uses **Groq API** for generating answers to the questions. It is a great example of combining **natural language processing** (NLP) and **streamlit** for creating interactive web apps.

## Features
- Users can submit one, two, or three article URLs.
- The app processes the content of the articles and presents a preview.
- Users can ask questions related to the content of the articles, and the app will generate appropriate answers using the **Groq API**.
- The app includes a process button to fetch and process the articles.

## Libraries and Technologies Used
- **Streamlit**: For building the web app interface.
- **Groq API**: For the question-answering model using `llama-3.3-70b-versatile`.
- **Unstructured**: For content extraction from the provided URLs.
- **LangChain**: For chaining operations like processing and retrieving answers.

## Setup and Installation

### Prerequisites
- Python 3.x
- A Groq API key (You can sign up for Groq and get a key from [here](https://groq.com/)).

### Steps to Run the App Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AshwathL/LLM-Article-Questioning-and-answering.git
   
   python -m venv venv

   venv\Scripts\activate

   cd ..

   cd ..

   pip install -r requirements.txt

   set GROQ_API_KEY=<your-api-key> 

   streamlit run app.py
   ```





