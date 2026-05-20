import os
from dotenv import load_dotenv
import google.generativeai as genai

from vectorstore.retriever import get_retriever
from llm.prompt import SYSTEM_PROMPT

# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

# =========================================================
# GET GOOGLE API KEY
# Works locally with .env
# Works on Streamlit Cloud with st.secrets
# =========================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

try:
    import streamlit as st

    if "GOOGLE_API_KEY" in st.secrets:
        GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

except Exception:
    pass

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Add it in .env locally or Streamlit Secrets during deployment."
    )

# =========================================================
# CONFIGURE GEMINI
# =========================================================

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(
    "gemini-flash-lite-latest"
)

# =========================================================
# RETRIEVER
# =========================================================

retriever = get_retriever()

# =========================================================
# DISCLAIMER
# =========================================================

DISCLAIMER = """
⚠️ DISCLAIMER:
This project is made only for AI/RAG knowledge purposes.
It does not constitute professional medical advice.
Always consult a qualified healthcare provider for diagnosis and treatment.
"""

# =========================================================
# MAIN FUNCTION
# =========================================================

def ask_healthcare_rag(question):

    docs = retriever.invoke(question)

    cleaned_docs = []
    sources = []

    for doc in docs:

        text = doc.page_content

        text = text.replace("\n", " ")
        text = " ".join(text.split())

        cleaned_docs.append(text)

        sources.append({
            "source": doc.metadata.get("source", "Unknown"),
            "content": text[:350]
        })

    context = "\n\n".join(cleaned_docs)

    context = context[:3000]

    final_prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question
    )

    try:

        response = model.generate_content(final_prompt)

        answer = response.text

    except Exception as e:

        answer = f"""
❌ Error generating response

{str(e)}

{DISCLAIMER}
"""

    return {
        "answer": answer,
        "sources": sources
    }