class QuizBrain:
    def __init__(self, _question_list):
        self.question_list=_question_list #it will be intialized by question_bank array
        self.question_number=0 #keeps track of which question the user is currently on
        self.score=0
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        current_question=self.question_list[self.question_number].text
        current_answer=self.question_list[self.question_number].answer
        self.question_number+=1
        user_input=input(f" Q.{self.question_number}: {current_question} 'true' or 'false' ?")
        self.check_answer(user_input, current_answer)

    def check_answer(self, _user_input, _correct_answer):
        if(_correct_answer.lower()==_user_input.lower()):
            self.score+=1
            print(f"correct. Your score is {self.score}/{self.question_number}. The correct answer is {_correct_answer}")
        else:
            print(f"incorrect. Your score is still {self.score}/{self.question_number}. The correct answer was {_correct_answer}")
        print("\n")

 
