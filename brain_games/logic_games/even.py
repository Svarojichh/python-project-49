from random import randint


CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_conditions():
    question_num = randint(1, 100)
    if question_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question_num, correct_answer
