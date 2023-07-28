#!/usr/bin/env python3

from random import randint, choice
import prompt
from operator import add, sub, mul

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    exp = ['+', '-', '*']
    random_exp = choice(exp) # рандом операторов
    random_num1, random_num2 = randint(1, 50), randint(1, 50) # рандом чисел
    question = str(random_num1) + ' ' + random_exp + ' ' + str(random_num2) # условие для игрока
    print('Question:', question) # вывод условия
    ops = { "+": add, "-": sub, "*": mul }
    result_question = ops[random_exp](random_num1, random_num2) # правильный ответ
    user_resp = prompt.integer() # ответ игрока
    print('Your answer:', user_resp) # вывод ответа игрока

    for i in range(1, 4):
            if user_resp == result_question:
                print('Correct!')
                if i == 3:
                    print(f'Congratulations, {name}!')
                    break
                random_exp = choice(exp) # рандом операторов
                random_num1, random_num2 = randint(1, 50), randint(1, 50) # рандом чисел
                question = str(random_num1) + ' ' + random_exp + ' ' + str(random_num2) # условие для игрока
                print('Question:', question) # вывод условия
                ops = { "+": add, "-": sub, "*": mul }
                result_question = ops[random_exp](random_num1, random_num2) # правильный ответ
                user_resp = prompt.integer() # ответ игрока
                print('Your answer:', user_resp) # вывод ответа игрока
            elif user_resp != result_question:
                print(f"{user_resp} is wrong answer ;(. Correct answer was {result_question}.\nLet's try again, {name}!")
                break

if __name__ == '__main__':
    main()
