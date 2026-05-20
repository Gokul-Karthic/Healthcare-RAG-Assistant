import pandas as pd

from sentence_transformers import SentenceTransformer, util

from llm.generator import ask_healthcare_rag

# ---------------------------------------------------
# EMBEDDING MODEL
# ---------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------------------------------------------
# TEST QUESTIONS
# ---------------------------------------------------

evaluation_data = [

    {
        "question": "What is hypertension?",
        "ground_truth": "Hypertension is high blood pressure."
    },

    {
        "question": "What are symptoms of severe hypertension?",
        "ground_truth": "Symptoms include headache, dizziness, chest pain, and blurred vision."
    }

]

# ---------------------------------------------------
# STORAGE
# ---------------------------------------------------

results = []

# ---------------------------------------------------
# EVALUATION LOOP
# ---------------------------------------------------

for item in evaluation_data:

    question = item["question"]
    ground_truth = item["ground_truth"]

    print(f"\nQuestion: {question}")

    try:

        response = ask_healthcare_rag(question)

        generated_answer = response["answer"]

        # -----------------------------------------
        # SEMANTIC SIMILARITY
        # -----------------------------------------

        emb1 = model.encode(generated_answer, convert_to_tensor=True)
        emb2 = model.encode(ground_truth, convert_to_tensor=True)

        similarity = util.cos_sim(emb1, emb2).item()

        print(f"\nGenerated Answer:\n{generated_answer}")

        print(f"\nGround Truth:\n{ground_truth}")

        print(f"\nSemantic Similarity Score: {similarity:.4f}")

        # -----------------------------------------
        # SAVE RESULTS
        # -----------------------------------------

        results.append({

            "question": question,
            "generated_answer": generated_answer,
            "ground_truth": ground_truth,
            "similarity_score": round(similarity, 4)

        })

    except Exception as e:

        print(f"\nError: {e}")

# ---------------------------------------------------
# DATAFRAME
# ---------------------------------------------------

df = pd.DataFrame(results)

print("\n\nFINAL EVALUATION RESULTS\n")

print(df)

# ---------------------------------------------------
# AVERAGE SCORE
# ---------------------------------------------------

if len(df) > 0:

    avg_score = df["similarity_score"].mean()

    print(f"\nAverage Similarity Score: {avg_score:.4f}")