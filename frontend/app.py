import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from llm.generator import ask_healthcare_rag


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Healthcare RAG Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main page */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #020617 100%);
        color: #f8fafc;
    }

    /* Hide Streamlit default footer */
    footer {
        visibility: hidden;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        border-right: 1px solid #1e293b;
    }

    /* Main title */
    .hero-title {
        font-size: 46px;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 26px;
        max-width: 850px;
        line-height: 1.6;
    }

    .badge {
        display: inline-block;
        background: rgba(14, 165, 233, 0.14);
        color: #7dd3fc;
        border: 1px solid rgba(125, 211, 252, 0.25);
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 13px;
        margin-right: 8px;
        margin-bottom: 8px;
    }

    .metric-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid #1e293b;
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }

    .metric-title {
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 6px;
    }

    .metric-value {
        font-size: 22px;
        font-weight: 700;
        color: #f8fafc;
    }

    .disclaimer-box {
        background: rgba(127, 29, 29, 0.28);
        border: 1px solid rgba(248, 113, 113, 0.35);
        padding: 16px;
        border-radius: 16px;
        color: #fecaca;
        margin-top: 18px;
        line-height: 1.5;
    }

    .source-card {
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 10px;
        color: #e2e8f0;
        line-height: 1.5;
    }

    .assistant-answer {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 20px;
        line-height: 1.7;
        box-shadow: 0 12px 28px rgba(0,0,0,0.22);
    }

    .small-muted {
        color: #94a3b8;
        font-size: 13px;
    }

    div[data-testid="stChatMessage"] {
        background: rgba(15, 23, 42, 0.38);
        border-radius: 18px;
        border: 1px solid rgba(51, 65, 85, 0.35);
        padding: 8px;
    }

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #334155;
        background: rgba(15, 23, 42, 0.75);
        color: #f8fafc;
        padding: 0.5rem 0.9rem;
    }

    .stButton > button:hover {
        border-color: #38bdf8;
        color: #7dd3fc;
        background: rgba(14, 165, 233, 0.13);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("## 🩺 Healthcare AI")
    st.markdown("Your AI-powered medical document assistant.")

    st.markdown("---")

    st.markdown("### ⚙️ System")
    st.markdown(
        """
        **LLM:** Gemini API  
        **Retriever:** FAISS  
        **Embeddings:** HuggingFace  
        **Chunking:** Semantic Chunking  
        **Interface:** Streamlit  
        """
    )

    st.markdown("---")

    st.markdown("### ✅ Features")
    st.markdown(
        """
        - Medical PDF retrieval  
        - Source-grounded answers  
        - Semantic search  
        - Clean response formatting  
        - Safety disclaimer  
        """
    )

    st.markdown("---")

    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")

    st.info(
        "This project is for AI/RAG learning purposes only. "
        "It is not a replacement for professional medical advice."
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="hero-title">Healthcare RAG Assistant</div>
    <div class="hero-subtitle">
        Ask healthcare-related questions and get answers grounded in uploaded medical documents.
        The system retrieves relevant context using semantic search and generates structured responses.
    </div>

    <span class="badge">RAG</span>
    <span class="badge">FAISS</span>
    <span class="badge">Semantic Search</span>
    <span class="badge">Gemini</span>
    <span class="badge">Medical PDFs</span>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Knowledge Source</div>
            <div class="metric-value">Medical PDFs</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Retrieval Engine</div>
            <div class="metric-value">FAISS Vector DB</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Answer Style</div>
            <div class="metric-value">Grounded AI</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# QUICK QUESTIONS
# =========================================================

st.markdown("### Try asking")

q1, q2, q3, q4 = st.columns(4)

with q1:
    if st.button("What is hypertension?", use_container_width=True):
        st.session_state.selected_question = "What is hypertension?"

with q2:
    if st.button("Symptoms of asthma", use_container_width=True):
        st.session_state.selected_question = "What are common symptoms of asthma?"

with q3:
    if st.button("Side effects of creatine", use_container_width=True):
        st.session_state.selected_question = "What are the possible side effects of creatine?"

with q4:
    if st.button("Fever causes", use_container_width=True):
        st.session_state.selected_question = "What are common causes of fever?"


# =========================================================
# CHAT HISTORY
# =========================================================

st.markdown("---")
st.markdown("## 💬 Medical Assistant Chat")

for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(chat["question"])

    with st.chat_message("assistant"):
        st.markdown(chat["answer"])

        if chat.get("sources"):
            with st.expander("📚 View retrieved sources"):
                for i, source in enumerate(chat["sources"], 1):
                    st.markdown(
                        f"""
                        <div class="source-card">
                            <b>Source {i}</b><br>
                            <span class="small-muted">{source["source"]}</span><br><br>
                            {source["content"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


# =========================================================
# INPUT HANDLING
# =========================================================

user_input = st.chat_input("Ask a healthcare-related question...")

if st.session_state.selected_question:
    prompt = st.session_state.selected_question
    st.session_state.selected_question = None
else:
    prompt = user_input


# =========================================================
# MAIN QUERY EXECUTION
# =========================================================

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching medical documents and generating answer..."):
            try:
                response = ask_healthcare_rag(prompt)

                answer = response.get("answer", "No answer generated.")
                sources = response.get("sources", [])

                st.markdown(
                    f"""
                    <div class="assistant-answer">
                    {answer}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if sources:
                    with st.expander("📚 Retrieved medical sources"):
                        for i, source in enumerate(sources, 1):
                            st.markdown(
                                f"""
                                <div class="source-card">
                                    <b>Source {i}</b><br>
                                    <span class="small-muted">{source["source"]}</span><br><br>
                                    {source["content"]}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                st.markdown(
                    """
                    <div class="disclaimer-box">
                    <b>DISCLAIMER:</b><br>
                    This project is made only for AI/RAG knowledge purposes. 
                    It does not constitute professional medical advice. 
                    Always consult a qualified healthcare provider for diagnosis and treatment.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.session_state.chat_history.append(
                    {
                        "question": prompt,
                        "answer": answer,
                        "sources": sources,
                        "time": str(datetime.now())
                    }
                )

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <p class="small-muted">
    Built using Retrieval-Augmented Generation with FAISS, semantic chunking, Gemini API, and Streamlit.
    </p>
    """,
    unsafe_allow_html=True
)