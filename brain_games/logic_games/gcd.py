from random import randint
from math import gcd


CONDITION = 'Find the greatest common divisor of given numbers.'


def game_conditions():
    random_num1, random_num2 = randint(1, 50), randint(1, 50)
    question_num = f"{random_num1} {random_num2}"
    correct_answer = gcd(random_num1, random_num2)
    return question_num, str(correct_answer)
