quiz_questions = {
    "What is the capital of nepal" : "Kathmandu",
    "What is the height of mount everest" : "8848",
    "where is IT bridge located" : "banepa",
    "At what age people are eligible for voting in nepal" : "18",
    "What is the capital of india" : "Delhi",
    "Name one framework of python" : "Django"
}

# questions = quiz_questions.keys()
# print(questions)



for i in range(len(quiz_questions)):
    Question = list(quiz_questions.keys())[i]
    print(Question)
    userInput = input("Enter answer")
    if userInput == list(quiz_questions.values())[i]:
        print("Your answer is correct")
    else:
        print("Your answer is not correct")

    