#!/usr/bin/env python3

from random import randint
import prompt


def main():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_num = randint(1, 100)
    print('Question:', random_num)
    user_resp = prompt.string()
    print('Your answer:', user_resp)

    for i in range(1, 4):
        if random_num % 2 == 0 and user_resp == 'yes' or random_num % 2 != 0 and user_resp == 'no':
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {name}!')
                break
            random_num = randint(1, 100)
            print('Question:', random_num)
            user_resp = prompt.string()
            print('Your answer:', user_resp)
        elif (random_num % 2 != 0 and user_resp == 'yes'):
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
        elif (random_num % 2 == 0 and user_resp == 'no'):
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            break
        else:
            print('Warning! Enter "yes" or "no".')
            break

if __name__ == '__main__':
    main()
