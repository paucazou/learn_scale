#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

import mingus
import random
import time
import util

def ask():
    """Ask one random question to user"""
    question = get_qna()
    start = time.time()
    answer = input(question[0]+' ')
    answer = [ x[0].upper() + x[1:] for x in answer.split()]
    if set(answer) != set(question[1]()):
        print("Error")
        print(question[1]())
    else:
        print("Right")
    
    end = time.time()
    print(f"Time: {end-start} seconds.")


def get_qna():
    key = util.get_random_key()
    questions = {
            f"What are the most important degrees in {key}?":lambda : util.find_degree(key,1,4,5),
            }
    return random.choice(list(questions.items()))

if __name__ == "__main__":
    ask()


