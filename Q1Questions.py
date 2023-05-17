import json

q = input("Input the multiple choice question: ")
answers = []
for i in range(4): answers.append(input(f"Answer ({i+1}): "))
ca = int(input("Input the index of the correct answer: "))

question_data = {
    "question": q,
    "answers": answers,
    "correct_answer": ca
}

with open("question.json", "w") as f:
    f.write(json.dumps(question_data))
