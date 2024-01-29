quiz_questions = {
    "What is the capital of nepal \n Kathmandu   Banepa   Panauti   Dhulikhel" : "Kathmandu",
    "What is the height of mount everest \n 1278   7863   7632   8848" : "8848",
    "where is IT bridge located \n Banepa   Panauti   Bhaktapur   Kathmandu" : "Banepa",
    "At what age people are eligible for voting in nepal \n 16   23   18   34" : "18",
    "What is the capital of india \n Kanpur   Delhi   Mumbai   Hydrabad" : "Delhi",
    "Name one framework of python \n Django   Flask   Panda   BeautifulSoup" : "Django"
}

# questions = quiz_questions.keys()
# print(questions)



for i in range(len(quiz_questions)):
    Question = list(quiz_questions.keys())[i]
    print(Question)
    userInput = input("Enter answer  ")
    if userInput == list(quiz_questions.values())[i]:
        print("Your answer is correct")
    else:
        print("Your answer is not correct")

    