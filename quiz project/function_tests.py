'''
    all testing and trial functions go here. For testing only.
'''

from question_model import Question
from data import question_data



question_bank=[]
for i in range(0, len(question_data)):
    question_text=question_data[i]['text']
    answer_text=question_data[i]['answer']
    new_question=Question(question_text, answer_text)
    question_bank.append(new_question)

question_bank_3=[]

for question in question_data:
    question_text=question["text"]
    answer_text=question["answer"]
    new_question=Question(question_text, answer_text)
    question_bank_3.append(new_question)

print(question_bank_3[0].text)

def next_question():
    score=0
    current_question=question_bank[0].text
    user_answer=input(f"{current_question} 'true' or 'false' ?").title()
    if user_answer!='True' and user_answer!='Talse':
        raise Exception
    if user_answer==question_bank[0].answer:
        score+=1
        print("greater happiness")
    else:
        print("no. That's not correct")
        

# for i in range(0, len(self.question_list)):
#             current_question=self.question_list[self.question_number].text
#             current_answer=self.question_list[self.question_number].answer
#             user_input=input(f" Q.{self.question_number+1}: {current_question} 'true' or 'false' ?").title()
#             if(user_input==current_answer):
#                 self.score+=1
#                 print(f"correct. Your score is {self.score}")
#             else:
#                 print(f"incorrect. Your score is {self.score}")
#             self.question_number+=1
# #retrieve the item at the current question number from question list
# Use input() to show the user the question text and ask for answer 

question = next_question()

print(question_bank[0].answer)

