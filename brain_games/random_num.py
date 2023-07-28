#!/usr/bin/env python3

from random import randint
import prompt
from math import gcd

def random_num():
    global random_num1, random_num2
    random_num1, random_num2 = randint(1, 50), randint(1, 50)
    print('Question:', random_num1, random_num2)
    global result_question
    result_question = gcd(random_num1, random_num2) # Правильный ответ
    global user_resp
    user_resp = prompt.integer()
    print('Your answer:', user_resp)
