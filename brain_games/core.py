import prompt


def core_games(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.CONDITION)
    count = 0
    while count < 3:
        count += 1
        question_num, correct_answer = game.games_brain()
        print('Question:', question_num)
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. \
Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
