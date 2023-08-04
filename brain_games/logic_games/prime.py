from random import randint


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        return "yes"
    else:
        return "no"


def game_conditions():
    question_num = randint(2, 100)
    correct_answer = is_prime(question_num)
    return question_num, correct_answer
