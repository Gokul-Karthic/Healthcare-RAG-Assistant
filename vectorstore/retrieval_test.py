from vectorstore.retriever import get_retriever

retriever = get_retriever()

query = "What are symptoms of diabetes?"

docs = retriever.invoke(query)

print("\nTop Retrieved Chunks:\n")

for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---\n")
    print(doc.page_content)