#!/usr/bin/env python3

from random import randint
import prompt
from brain_games import greeting


def main():
    greeting.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    random_num = randint(1, 100)
    print('Question:', random_num)
    k = 0
    for i in range(2, random_num // 2+1):
        if (random_num % i == 0):
            k = k+1
    if (k <= 0):
        result = "yes"
    else:
        result = "no"
    # print(result)  # тестовый правельный ответ
    user_resp = prompt.string()
    print('Your answer:', user_resp)

    for i in range(1, 4):
        if user_resp == result:
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {greeting.name}!')
                break
            random_num = randint(1, 100)
            print('Question:', random_num)
            k = 0
            for i in range(2, random_num // 2+1):
                if (random_num % i == 0):
                    k = k+1
            if (k <= 0):
                result = "yes"
            else:
                result = "no"
            # print(result)  # тестовый правельный ответ
            user_resp = prompt.string()
            print('Your answer:', user_resp)
        elif user_resp == 'yes' and result == 'no':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {greeting.name}!")
            break
        elif user_resp == 'no' and result == 'yes':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {greeting.name}!")
            break
        else:
            print('Warning! Enter "yes" or "no".')
            break


if __name__ == '__main__':
    main()
