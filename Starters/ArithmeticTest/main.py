"""
A primary school teacher wants a program to test the basic arithmetic skills of her students.
Generate questions (2 numbers only) consisting of addition, subtraction, multiplication and division
The system should ask the student's name and then ask 10 questions.
The program should feedback if the answers are correct, and then generate a final score at the end.

Extensions:
1. Extend your program so that it stores the results somwhere.
The teacher has three classes and needs to distinguish between them.
2. The teacher wants to log student performance.
The program should store the last three scores for each student and output them in descending order.
"""

import random
from werkzeug.security import secure_filename

def quiz():
    """Quiz the user on basic arithmetic"""
    score = 0
    data = []
    user = input('Please enter your name: ')
    user_class = input('Please enter your class: ')

    for _ in range(0, 10):
        first = random.randint(1, 100)
        second = random.randint(1, 100)
        sign = random.randint(1, 4)

        if sign == 1:
            print(f'What is {first}+{second}?')
            answer = round(float(input('Answer: ')))
            correct = round(first + second)
            data.append({'question': f'{first}+{second}', 'student': answer, 'answer': correct})
            if correct == answer:
                print('Correct!')
                score += 1
            else:
                print('Incorrect!')
        elif sign == 2:
            print(f'What is {first}-{second}?')
            answer = round(float(input('Answer: ')))
            correct = round(first - second)
            data.append({'question': f'{first}-{second}', 'student': answer, 'answer': correct})
            if correct == answer:
                print('Correct!')
                score += 1
            else:
                print('Incorrect!')
        elif sign == 3:
            print(f'What is {first}*{second}?')
            answer = round(float(input('Answer: ')))
            correct = round(first * second)
            data.append({'question': f'{first}*{second}', 'student': answer, 'answer': correct})
            if correct == answer:
                print('Correct!')
                score += 1
            else:
                print('Incorrect!')
        elif sign == 4:
            print(f'What is {first}/{second}?')
            answer = round(float(input('Answer: ')), 2)
            correct = round(first / second, 2)
            data.append({'question': f'{first}/{second}', 'student': answer, 'answer': correct})
            if correct == answer:
                print('Correct!')
                score += 1
            else:
                print('Incorrect!')

    print(f'Your score is {score}/10 {user}')
    with open(secure_filename(f'{user_class}/{user}.txt'), 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f'''
Question: {item["question"]}
Student\'s answer: {item["student"]}
Correct answer: {item["answer"]}
''')
        file.write(f'Score is {score}/10')

def check_scores():
    """Check the scores of the students"""
    while True:
        user_class = input('Please enter the class you want to check: ')
        user = input('Please enter the student you want to check: ')
        if user_class == 'exit' or user == 'exit':
            break
        with open (f'{user_class}/{user}.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line)


VALID = False
while not VALID:
    permission = input('Are you a student or a teacher?\n1) Teacher\n2) Student\n>>> ')
    if permission == '1':
        VALID = True
        check_scores()
    elif permission == '2':
        VALID = True
        quiz()
    else:
        print('Invalid input')
