from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_medical_pdfs(path="data/raw_pdfs"):
    loader = PyPDFDirectoryLoader(path)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    return documents