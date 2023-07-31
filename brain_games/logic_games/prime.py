from random import randint


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def games_brain():
    question_num = randint(1, 100)
    k = 0
    for i in range(2, question_num // 2 + 1):
        if (question_num % i == 0):
            k = k + 1
    if (k <= 0):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question_num, correct_answer
