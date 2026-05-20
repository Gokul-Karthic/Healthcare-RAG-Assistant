<div align="center">

# 🏥 Healthcare Document Assistant
### *An AI-powered medical Q&A system built on Retrieval-Augmented Generation*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-RAG_Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-0467DF?style=for-the-badge&logo=meta&logoColor=white)](https://faiss.ai)
[![Gemini](https://img.shields.io/badge/Google_Gemini-LLM-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)

<br/>


<br/>

</div>

---
### *LIVE DEMO : https://healthcare-rag-assistant-gokul-karthic.streamlit.app *


##  What Is This Project?

This is an **AI-powered healthcare document assistant** that lets you ask plain-English questions about health topics — symptoms, diseases, prevention, medications, and more — and get answers that are actually **grounded in trusted medical documents**.

Most AI chatbots answer from memory alone. This one is different. It **reads your documents first**, finds the most relevant pieces of information, and *then* generates an answer. That approach has a name: **Retrieval-Augmented Generation (RAG)** — and it's one of the most important patterns in modern AI engineering.

This project was built to solve a real problem: **LLMs hallucinate**, and in a domain like healthcare, that's not acceptable.

---

##  Why Build This?


- **Hallucinations are dangerous in healthcare.** An LLM confidently giving wrong medical information can cause real harm. This project directly tackles that by anchoring every answer to actual document content.
- **RAG is the industry standard.** Nearly every production AI system that needs reliable, up-to-date, or domain-specific knowledge uses some form of RAG. Building one from scratch is how you truly understand it.
- **It's a complete, deployable AI system** — not just a notebook. Embeddings, vector search, prompt engineering, LLM integration, and a live frontend all working together.


---

##  What Even Is RAG?


A regular LLM is like asking a friend who's read a lot of books but might misremember things. A **RAG system** is like giving that same friend your specific documents to read *right before* they answer. They're no longer relying on memory — they're working from the material in front of them.

```
Your Question
     │
     ▼
┌─────────────────────┐
│  Semantic Retrieval  │  ← Finds the most relevant chunks from your PDFs
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│  Prompt Construction │  ← Wraps the question + retrieved context together
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│     Gemini LLM       │  ← Generates an answer grounded in that context
└─────────────────────┘
     │
     ▼
Structured Answer + Sources + Disclaimer
```

The result is an AI that's **far less likely to make things up**, because it's told exactly what it's allowed to say.

---

## 🏗️ System Architecture

Here's how the full pipeline works from document to answer:

```
📄 Healthcare PDFs
        │
        ▼
  PDF Text Extraction
        │
        ▼
  Semantic Chunking          ← Splits text by meaning, not arbitrary character count
        │
        ▼
  Text Embeddings            ← Converts chunks into numerical vectors
        │
        ▼
  FAISS Vector Database      ← Stores and indexes those vectors for fast search
        │
        │ ◄── User submits a question
        ▼
  Semantic Retrieval         ← Finds chunks most similar to the question
        │
        ▼
  Prompt Construction        ← Injects retrieved chunks into the LLM prompt
        │
        ▼
  Google Gemini API          ← Generates a structured, readable answer
        │
        ▼
  📋 Answer + Sources + Medical Disclaimer
```

Every step in this pipeline is intentional. Nothing is left to chance or blind generation.

---

##  Features

###  Medical PDF Question Answering
Ask anything covered by the uploaded healthcare documents. The system finds the right sections and uses them to craft the answer.

```
"What is hypertension?"
"What are the symptoms of asthma?"
"Explain diabetes in simple terms."
"What are the side effects of creatine?"
```

###  Semantic Search (Not Just Keywords)
The system understands *meaning*, not just matching words. So if you ask about **"high blood pressure"**, it can correctly retrieve content about **"hypertension"** — because the embeddings know they mean the same thing.

###  Semantic Chunking
Most RAG tutorials split documents every N characters. This project does it better — chunks are created based on **semantic boundaries** (meaning and context). This leads to:
- More coherent retrieved chunks
- Better answer quality
- Stronger grounding for the LLM

###  FAISS Vector Database
All document embeddings are stored in a **FAISS index**, enabling lightning-fast similarity search at scale. No slow brute-force comparisons.

###  Gemini-Powered Generation
The LLM backend is **Google Gemini** (`gemini-flash-lite-latest`), chosen for being:
- Fast and responsive
- Free-tier friendly
- Well-suited to structured, readable responses
- Efficient for RAG-style prompts

###  Source-Grounded Answers
Every answer comes with the **source chunks it was built from**, displayed in expandable sections. Users can see exactly where the information came from — no black box.

###  Built-in Medical Disclaimer
The app surfaces a clear, persistent disclaimer:
> *This project is built for AI/RAG learning purposes only. It is not a substitute for professional medical advice. Always consult a qualified healthcare provider.*

This isn't an afterthought — responsible AI in healthcare means making limitations visible.

###  Polished Streamlit Frontend
The UI isn't just functional — it's designed to feel good to use:
- Clean, modern layout
- Sidebar navigation
- Quick-question buttons for instant exploration
- Chat-style answer interface
- Expandable source sections
- Disclaimer panel

###  Deployed & Publicly Accessible
The application is live on **Streamlit Community Cloud** — shareable via a public URL, no setup required for end users.

---

##  Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **Frontend** | Streamlit |
| **LLM** | Google Gemini API (`gemini-flash-lite-latest`) |
| **Embeddings** | HuggingFace Sentence Transformers |
| **Vector Database** | FAISS |
| **RAG Framework** | LangChain |
| **PDF Loading** | PyPDF / LangChain Document Loaders |
| **Chunking Strategy** | Semantic Chunking |
| **Deployment** | Streamlit Community Cloud |
| **Secrets Management** | python-dotenv / Streamlit Secrets |

---

##  Concepts Demonstrated

This project isn't just about the code — it's a practical demonstration of a wide set of AI/ML concepts:

**Foundations**
- Large Language Models and how they work
- Natural Language Processing pipelines
- Embeddings and vector representations of text

**RAG-Specific**
- Retrieval-Augmented Generation end-to-end
- Semantic similarity search
- Vector databases and indexing
- Semantic chunking strategies
- Prompt engineering and context injection
- Hallucination reduction through document grounding
- Source attribution and answer transparency

**Engineering**
- Full-stack AI application development
- API integration (Gemini, HuggingFace)
- Environment variable management
- Cloud deployment

---


##  Example Questions to Try

Once the app is running, here are some questions worth asking:

```
→ What are the early symptoms of diabetes?
→ How does high blood pressure damage the heart over time?
→ What is the difference between a migraine and a tension headache?
→ What does low ferritin indicate?
→ What are the side effects of taking creatine daily?
→ How does the body respond to a fever?
→ What lifestyle changes help with GERD?
→ What does persistent fatigue usually mean?
```

---

##  Important Disclaimer

> **This application is built purely for educational and AI/RAG learning purposes.**
>
> It is **not** a medical device, clinical tool, or substitute for professional healthcare advice.
> The information retrieved and generated by this system may be incomplete or context-dependent.
> **Always consult a qualified, licensed healthcare professional** for any personal health concerns, diagnosis, or treatment decisions.

---


---

<div align="center">

**Built with curiosity, caffeine, and a genuine belief that AI can make healthcare information more accessible — responsibly.**

<br/>

</div>
