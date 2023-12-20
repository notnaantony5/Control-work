import json


class Question:
    def __init__(self,
                 question: str,
                 answer: str,
                 points: int):
        self.question = question
        self.answer = answer
        self.points = points

    def check(self, answer: str):
        return (self.answer.strip().lower()
                == answer.strip().lower())


class User:
    def __init__(self, name):
        self.name = name
        self.points = 0
        print("Привет, это викторина!")

    def get_answer(self, question: Question):
        answer = input(
            f"Вопрос:\n"
            f"{question.question}\n"
            f":"
        )
        return answer

    def feedback(self,
                 question: Question,
                 positive=True):
        if positive:
            self.points += question.points
            print(f"Верный ответ!\n"
                  f"Вы получили {question.points} "
                  f"баллов!")
        else:
            print(f"Ответ неверный!\n"
                  f"Правильный ответ: "
                  f"{question.answer}")

    def end(self):
        print(f"Поздравляю, {self.name}!"
              f"Вы набрали {self.points} баллов")


class Quiz:
    def __init__(self, filehandler):
        name = input("Введите имя: ")
        self.user = User(name)
        self.fh = filehandler
        self.questions = self.fh.read()


    def game(self):
        for question in self.questions:
            answer = self.user.get_answer(question)
            result = question.check(answer)
            self.user.feedback(question, positive=result)
        self.user.end()

class JSONReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return [
                Question(**question)
                for question in json.load(f)
            ]


class CSVReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
            names = lines[0].split(',')
            data = [
                {
                    name: value
                    for name, value in
                    zip(names, line.split(','))
                }
                for line in lines[1:]
            ]
            return [
                Question(**question)
                for question in data
            ]
