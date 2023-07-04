class QuizBrain:
    def __init__(self,question_bank):
        self.quesiton_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.quesiton_number]
        self.quesiton_number += 1
        user_answer = input(f"Q.{self.quesiton_number}: {current_question.text} True/False: ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):
        if self.quesiton_number < len(self.question_list):
            return True
        else:
            return False
               
    def check_answer(self,user_answer,answer):
        if user_answer.lower()==answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
        print(f"Your current score is {self.score}/{self.quesiton_number}")
        print("")
