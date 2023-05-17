import json

with open("questions.txt", "r") as file:
    q = file.readlines()

score = 0

for i in range(0, len(q), 7):
    question_data = {
        "question": q[i].strip(),
        "answers": {
            "A": q[i+1].strip(),
            "B": q[i+2].strip(),
            "C": q[i+3].strip(),
            "D": q[i+4].strip()
        },
        "correct_answer": q[i+5].strip()
    }

    print("\nQuestion:", question_data["question"])
    print("A:", question_data["answers"]["A"])
    print("B:", question_data["answers"]["B"])
    print("C:", question_data["answers"]["C"])
    print("D:", question_data["answers"]["D"])

    user_answer = input("Enter your answer (A/B/C/D): ")

    if user_answer.upper() == question_data["correct_answer"]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print("\nQuiz completed!")
print("Your score:", score, "out of", len(q) // 7)
