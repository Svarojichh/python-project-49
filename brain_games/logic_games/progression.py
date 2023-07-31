from random import randint, choice


CONDITION = 'What number is missing in the progression?'


def games_brain():
    progression = list(range(randint(1, 20), 1000, randint(1, 30)))
    progression_len = progression[:10]
    correct_answer = choice(progression_len)
    index = progression_len.index(correct_answer)
    progression_len[index] = ".."
    question_num = " ".join(str(x) for x in progression_len)
    return question_num, str(correct_answer)
