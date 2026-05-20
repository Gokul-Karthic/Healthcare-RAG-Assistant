from llm.generator import ask_healthcare_rag

question = "What are symptoms of hypertension?"

response = ask_healthcare_rag(question)

print("\nANSWER:\n")
print(response["answer"])

print("\nSOURCES:\n")

for source in response["sources"]:
    print(source["source"])