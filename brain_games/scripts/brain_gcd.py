#!/usr/bin/env python3


from brain_games import greeting
from brain_games import random_num


def main():
    greeting.greeting()  # greeting and global name
    print("Find the greatest common divisor of given numbers.")
    random_num.random_num()
    i = 1
    while random_num.user_resp == random_num.result_question:
        print("Correct!")
        i += 1
        random_num.random_num()
        if random_num.user_resp == random_num.result_question and i == 3:
            print("Correct!")
            print(f"Congratulations, {greeting.name}!")
            break
    else:
        print(f"{random_num.user_resp} is wrong answer ;(. \
            Correct answer was {random_num.result_question}.")
        print(f"Let's try again, {greeting.name}!")


if __name__ == '__main__':
    main()
