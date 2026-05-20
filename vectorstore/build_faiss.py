from langchain_community.vectorstores import FAISS

from ingestion.pdf_loader import load_medical_pdfs
from ingestion.chunker import split_documents
from ingestion.embedder import embeddings


def create_vector_store():

    documents = load_medical_pdfs()

    print(f"Loaded {len(documents)} pages")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vectorstore.save_local("vectorstore/faiss_index")

    print("FAISS index saved")


if __name__ == "__main__":
    create_vector_store()