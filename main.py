#Importing te Questions class
from Question import Questions

#These are the set of questions to be asked stored in an array
question_prompt = [
    'What is the capital city of Kenya?\n(A)Kisumu\n(B)Mombasa\n(C)Nairobi\n',
    'How many Counties are there in Kenya?\n(A)50\n(B)47\n(C)10\n',
    'Who is the current president of Kenya?\n(A)Hon.Uhuru\n(B)Hon.Wajackoya\n(C)Hon.Ruto\n'
]

#Another array of questions calling the Questions class
question = [
    Questions(question_prompt[0], 'C'),
    Questions(question_prompt[1], 'B'),
    Questions(question_prompt[2], 'A')
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + ' Correct!')

run_test(question)