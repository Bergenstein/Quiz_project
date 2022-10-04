import question_model, data, quiz_brain
from art import logo as logo

print(logo)
question_data = data.question_data

question_bank = []
for i in range(0, len(question_data)):
  new_question = question_model.Question(question_data[i]["question"],
                                         question_data[i]["correct_answer"])
  question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)

while (quiz.still_has_questions()):
  quiz.next_question()

if (not quiz.still_has_questions()):
  print(
    f"quiz is finished. Your final score is {quiz.score}/{len(quiz.question_list)}"
  )
