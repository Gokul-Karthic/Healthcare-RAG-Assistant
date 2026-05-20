from langchain_experimental.text_splitter import SemanticChunker
from ingestion.embedder import embeddings


def split_documents(documents):

    text_splitter = SemanticChunker(
        embeddings=embeddings,
        breakpoint_threshold_type="percentile",
        breakpoint_threshold_amount=80
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} semantic chunks")

    return chunks