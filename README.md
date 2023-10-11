# Web Page Question Answering

# Web Page QA App

This is a simple Python application that enables you to extract content from a static web page and ask questions about its content. The application leverages OpenAI's API and llama-index for question-answering and is built using Streamlit and various Python libraries.

## Getting Started

Before running the application, make sure you have the necessary dependencies installed and set up your environment.

### Prerequisites

You'll need the following Python libraries installed:

- `dotenv`: For loading environment variables.
- `openai`: The OpenAI API for question answering.
- `llama_index`: LlamaIndex is a data framework for LLM applications to ingest, structure, and access data.
- `streamlit`: A Python web app framework for building user interfaces.

You can install these libraries using `pip`:

```bash
pip install python-dotenv openai llama_index streamlit
```

### Environment Setup

To use the OpenAI API, you'll need to set your API key in a `.env` file in the same directory as your project. You can obtain an API key from the OpenAI website.

```dotenv
# .env

OPENAI_API_KEY=your_api_key_here
```

## Running the Application

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start a local development server, and you can access the app in your web browser.

## How to Use

1. Enter a URL: In the application, you'll see a text input field where you can enter the URL of a static web page.

2. Fetch Web Page Content: Once you enter a URL, the application will fetch the content from the web page and store it on your local disk.

3. Ask Questions: Enter your questions in the text input field labeled "Ask your question."

4. Get Answers: Click the "Ask" button to submit your question. The application will use the OpenAI API and the `llama_index` library to find answers to your question by using the web page's content as context.

## Note

This is a basic example of a web page question answering app, and it can also be extended and customized to suit your specific needs. Please be aware that the accuracy of the answers may vary depending on the content of the web page and the complexity of the questions. Test it with different web pages and questions to evaluate its performance.