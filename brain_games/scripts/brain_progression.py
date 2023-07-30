#!/usr/bin/env python3

from random import randint, choice
import prompt
from brain_games import greeting


def main():
    greeting.greeting()
    print("What number is missing in the progression?")
    progression = list(range(randint(1, 20), 1000, randint(1, 30)))
    progression_len = progression[:10]
    random_choice = choice(progression_len)
    index = progression_len.index(random_choice)
    progression_len[index] = ".."
    progression_len = " ".join(str(x) for x in progression_len)
    print("Question:", progression_len)
    # print("Тестовый правильный ответ:",random_choice)
    user_resp = prompt.integer()
    print('Your answer:', user_resp)

    i = 1
    while user_resp == random_choice:
        print("Correct!")
        i += 1
        progression = list(range(randint(1, 20), 1000, randint(1, 30)))
        progression_len = progression[:10]
        random_choice = choice(progression_len)
        index = progression_len.index(random_choice)
        progression_len[index] = ".."
        progression_len = " ".join(str(x) for x in progression_len)
        print("Question:", progression_len)
        # print("Тестовый правильный ответ:",random_choice)
        user_resp = prompt.integer()
        print('Your answer:', user_resp)
        if user_resp == random_choice and i == 3:
            print("Correct!")
            print(f"Congratulations, {greeting.name}!")
            break
    else:
        print(f"{user_resp} is wrong answer ;(. \
            Correct answer was {random_choice}.")
        print(f"Let's try again, {greeting.name}!")


if __name__ == '__main__':
    main()
