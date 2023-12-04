class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):  # задає наступне запитання провіряє відповідь
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text}. (True/False)?:")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, right_answer):  # провіряє чи правильна відповідь
        if user_answer == right_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
            print(f"correct answer was {right_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
