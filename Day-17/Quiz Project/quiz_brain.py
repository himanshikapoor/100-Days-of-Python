class QuizBrain:
    def __init__(self, question_bank):
        self.score = 0
        self.question_number = 0
        self.question_list = question_bank

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        ques = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f'Q{self.question_number}: {ques.text} (True/False) ')
        self.check_answer(guess, ques.answer)

    def check_answer(self, guess, correct_answer):
        if guess.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def display_final_score(self):
        print("You've completed the quiz.")
        print(f"Your final score is {self.score}/{self.question_number}")
