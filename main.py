from classes import Quiz, JSONReader, CSVReader

if __name__ == "__main__":
    quiz = Quiz(CSVReader("questions.csv"))
    quiz.game()
