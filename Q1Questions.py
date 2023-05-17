import json

q = input("Input the multiple choice question: ")
a = input("Input option A: ")
b = input("Input option B: ")
c = input("Input option C: ")
d = input("Input option D: ")
ca = input("Input the letter of the correct answer: ")

question_data = {
    "question": q,
    "answers": {
        "A": a,
        "B": b,
        "C": c,
        "D": d
    },
    "correct_answer": ca
}

with open("questions.json", "a") as file:
    json.dump(question_data, file)
    file.write("\n")
