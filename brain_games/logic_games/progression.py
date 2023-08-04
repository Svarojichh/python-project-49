from random import randint, choice


CONDITION = 'What number is missing in the progression?'


def game_conditions():
    progression = list(range(randint(1, 20), 1000, randint(1, 30)))
    len_progression = 10
    question_selection = progression[:len_progression]
    correct_answer = choice(question_selection)
    index = question_selection.index(correct_answer)
    question_selection[index] = ".."
    question_num = " ".join(str(x) for x in question_selection)
    return question_num, str(correct_answer)
