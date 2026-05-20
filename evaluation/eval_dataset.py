from datasets import Dataset

from evaluation.sample_questions import questions
from llm.generator import ask_healthcare_rag


def build_dataset():

    data = {
        "question": [],
        "answer": [],
        "contexts": [],
        "ground_truth": []
    }

    for item in questions:

        response = ask_healthcare_rag(item["question"])

        answer = response["answer"]

        contexts = [
            source["content"]
            for source in response["sources"]
        ]

        data["question"].append(item["question"])
        data["answer"].append(answer)
        data["contexts"].append(contexts)
        data["ground_truth"].append(item["ground_truth"])

    return Dataset.from_dict(data)