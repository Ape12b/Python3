class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.current_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1} {self.question_list[self.question_number].text} "
                            f"(True/False): ").lower()
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.current_score += 1
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.current_score}/{self.question_number + 1}")

        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.current_score}/{self.question_number + 1}")
