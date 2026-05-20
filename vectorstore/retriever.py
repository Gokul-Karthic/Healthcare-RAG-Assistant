from langchain_community.vectorstores import FAISS
from ingestion.embedder import embeddings


def get_retriever():

    db = FAISS.load_local(
        "vectorstore/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever