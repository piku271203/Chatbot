# GenAI-ChatBot: A Q&A Chatbot powered by LangChain and Groq

A simple and powerful question-answering chatbot built with Streamlit, LangChain, and the Groq API. This chatbot allows you to get clear, concise, and precise answers to your questions, using state-of-the-art Llama models.

## Features

- Interactive and user-friendly web interface built with Streamlit.
- Powered by the fast Groq API and LangChain for language model orchestration.
- Choice of different Llama models (llama-3.1-8b-instant, llama-3.1-8b, llama-3.1-8b-chat).
- Secure API key handling.
- Easy to set up and run locally.

## Getting Started

### Prerequisites

- Python 3.7+
- An API key from [Groq](https://console.groq.com/keys).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/abhijit1901/genAI-ChatBot.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd genAI-ChatBot
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the Streamlit application:
    ```bash
    streamlit run 1-Langchainbasic/qachatbot.py
    ```
2.  Open your browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).
3.  Enter your Groq API key in the sidebar.
4.  Start chatting!

## Built With

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/)
