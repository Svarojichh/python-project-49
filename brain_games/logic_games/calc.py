from random import randint, choice
from operator import add, sub, mul


CONDITION = 'What is the result of the expression?'


def games_brain():
    exp = ['+', '-', '*']
    random_exp = choice(exp)
    random_num1, random_num2 = randint(1, 50), randint(1, 50)
    question_num = f"{str(random_num1)} {random_exp} {str(random_num2)}"
    ops = {"+": add, "-": sub, "*": mul}
    correct_answer = ops[random_exp](random_num1, random_num2)
    return question_num, str(correct_answer)
