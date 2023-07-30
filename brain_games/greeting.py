#!/usr/bin/env python3

import prompt


def greeting():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
