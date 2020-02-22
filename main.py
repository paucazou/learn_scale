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
    if check_answer(answer,question[1]):
        print("Error")
        print(question[1]())
    else:
        print("Right")
    
    end = time.time()
    print(f"Time: {end-start} seconds.")

def check_answer(answer,answer_expected) -> bool:
    """Check the validity of an answer"""
    try:
        return set(answer) != set(answer_expected)
    except TypeError:
        return answer == answer_expected


def get_qna():
    # random data
    key = util.get_random_key()
    function = random.choice(util.functions)
    note = random.choice(util.find_degree(key,*range(1,8)))
    degree = random.choice(range(1,8))
    s_or_b = "#" if random.randrange(2) else "b"

    questions = {
            f"What are the most important degrees in {key}?":lambda : util.find_degree(key,1,4,5),
            f"What is the {function} in {key}?":lambda : util.find_function(key,function),
            f"What is the degree of {note} in {key}?":lambda : util.get_degree_of(key,note),
            f"What is {degree} in {key}?":lambda : util.find_degree(key,degree),
            f"How many accidentals for {key}?":lambda : len(util.get_accidentals(key)),
            f"What is the key signature of {key}?":lambda : util.get_accidentals(key),
            f"What are the accidentals not in the key signature of {key}?":lambda : util.get_minor_accidentals(key) if key.islower() else "",
            f"To which scales {note} can belong to?":lambda : util.determine_note_scale(note),
            f"What is the {function} chord in {key}?":lambda : util.find_function_chord(key,function),
            f"What is the relative of {key}?":lambda : util.get_relative(key),
            f"What is the closely related key with a {s_or_b} more of {key}?":lambda : util.find_function("dominant" if s_or_b == "#" else "subdominant"),
            f"What is the closely related key with a {s_or_b} more of the relative of {key}?":lambda : util.find_function(util.get_relative(key),"dominant" if s_or_b == "#" else "subdominant"),
            f"What is the diminished chord of {key}?":lambda : util.build_diminished_chord(key),
            f"What is the augmented chord of {key}?":lambda : util.build_augmented_chord(key),

            }

    return random.choice(list(questions.items()))

if __name__ == "__main__":
    ask()


