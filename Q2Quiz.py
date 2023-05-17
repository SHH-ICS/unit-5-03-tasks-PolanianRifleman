import json

with open("question.json", "r") as f:
    d = json.loads(f.read())

while True:

    print("")
    print(d["question"])
    print("\nAnswer 1:",(d["answers"][0]))
    print("Answer 2:",(d["answers"][1]))
    print("Answer 3:",(d["answers"][2]))
    print("Answer 4:",(d["answers"][3]))

    b = int(input("\nWhat is the correct answer \n(example: if the correct answer is (Answer 3) type 3)\nType your answer here: "))

    if b == (d["correct_answer"]):
        print("\nWell done, your answer was correct! \n\n(Run the python file again if you would like to do the quiz again)\n")
        break
    elif b != (d["correct_answer"]):
        print("\nIncorrect! Please try again!")