#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

import os
import requests
from bs4 import BeautifulSoup
import streamlit as st
from groq import Groq

# Set the API key directly in the code (if you haven't set the environment variable)
os.environ["GROQ_API_KEY"] = "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"

# Function to fetch and extract content from the URLs using BeautifulSoup
def fetch_content(urls):
    documents = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Try to find the main content by targeting <article>, <p>, or other relevant tags
            article_content = ""
            
            article_tag = soup.find("article")
            if article_tag:
                article_content = article_tag.get_text(separator=" ").strip()
            else:
                paragraphs = soup.find_all("p")
                for p in paragraphs:
                    article_content += p.get_text(separator=" ").strip() + " "
            
            article_content = article_content.replace("\n", " ").replace("\r", "").strip()

            if article_content:
                documents.append({"url": url, "content": article_content})
            else:
                st.warning(f"Could not extract content from {url}")
        except Exception as e:
            st.error(f"Error fetching content from {url}: {str(e)}")
    return documents

# Function to get a response from Groq (with content trimming)
def get_groq_answer(question, documents):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    # Combine the content of all documents, but trim it to avoid exceeding token limits
    combined_content = " ".join([doc['content'][:1000] for doc in documents])  # Limit each document's content to 1000 characters
    
    # If the content is still too long, you can trim further or handle more carefully
    if len(combined_content.split()) > 6000:
        combined_content = " ".join(combined_content.split()[:6000])  # Limit total content to 6000 tokens
    
    # Request a response from Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an assistant that answers questions based on the provided articles."},
            {"role": "user", "content": f"{question} \n\n{combined_content}"}
        ],
        model="llama-3.3-70b-versatile",
    )
    
    return chat_completion.choices[0].message.content

# Streamlit app UI
st.title("LLM Question Answering from Articles")
st.write("Provide three article URLs, and ask questions related to them.")

url1 = st.text_input("Enter the URL of the first article:")
url2 = st.text_input("Enter the URL of the second article:")
url3 = st.text_input("Enter the URL of the third article:")

urls = [url1, url2, url3]


if any(urls):
    st.write("Fetching and processing articles...")

    documents = fetch_content(urls)

    if documents:
        st.write(f"Processed {len(documents)} documents.")
        
        # Display the content for each document
        for i, doc in enumerate(documents):
            st.write(f"Document {i+1}: {doc['url']}")
            st.write(doc['content'][:500])  # Display a preview of the first 500 characters

        # Ask a question related to the articles
        question = st.text_input("Ask a question related to the articles:")

        if question:
            st.write("Generating answer...")
            answer = get_groq_answer(question, documents)
            st.write("Answer:")
            st.write(answer)
    else:
        st.warning("No articles were processed successfully.")
else:
    st.warning("Please provide all three article URLs.")
