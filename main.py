#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

import mingus
import random
import sys
import time
import util


def ask():
    """Ask one random question to user"""
    question = get_qna()
    start = time.time()
    answer = input(question[0]+' ')
    answer = [ x[0].upper() + x[1:] for x in answer.split()]
    if not check_answer(answer,question[1]):
        print("Error")
        print(question[1]())
    else:
        print("Right")
    
    end = time.time()
    print(f"Time: {end-start} seconds.")

def multiple_questions(nb):
    """Ask nb questions
    We do not need to ask as many questions as specified
    in nb since ask is called at least once more"""
    for i in range(nb):
        ask()

def check_answer(answer,answer_expected) -> bool:
    """Check the validity of an answer"""
    try:
        return set(answer) == set(answer_expected)
    except TypeError:
        return answer == answer_expected


def get_qna(i=False):
    """Get one random question and answer
    If i is set to an integer, return the matching question
    """
    # random data
    key = util.get_random_key()
    function = random.choice(util.functions)
    note = random.choice(util.find_degree(key,*range(1,8)))
    degree = random.choice(range(1,8))
    s_or_b = "#" if util.randbool() else "b"
    seventh = util.randbool()
    func_deg = random.choice(util.functions + util.degrees)
    chord = util.build_chord(key,func_deg,seventh)

    questions = {
            f"What are the most important degrees in {key}?":lambda : util.find_degree(key,1,4,5),
            f"What is the {function} in {key}?":lambda : util.find_function(key,function),
            f"What is the degree of {note} in {key}?":lambda : util.get_degree_of(key,note),
            f"What is {degree} in {key}?":lambda : util.find_degree(key,degree),
            f"How many accidentals for {key}?":lambda : len(util.get_accidentals(key)),
            #6
            f"What is the key signature of {key}?":lambda : util.get_accidentals(key),
            f"What are the accidentals not in the key signature of {key}?":lambda : util.get_minor_accidentals(key) if key.islower() else "",
            f"To which scales {note} can belong to?":lambda : util.determine_note_scale(note),
            f"What is the {function} chord in {key}?":lambda : util.find_function_chord(key,function),
            f"What is the relative of {key}?":lambda : util.get_relative(key),
            # 11
            f"What is the closely related key with a {s_or_b} more of {key}?":lambda : util.find_function(key,"dominant" if s_or_b == "#" else "subdominant"),
            f"What is the closely related key with a {s_or_b} more of the relative of {key}?":lambda : util.find_function(util.get_relative(key),"dominant" if s_or_b == "#" else "subdominant"), 
            f"What is the diminished chord of {key}?":lambda : util.build_diminished_chord(key),
            f"What is the augmented chord of {key}?":lambda : util.build_augmented_chord(key),
            f"What are the notes of the parallel scale of {key}?":lambda : util.get_parallel(key).ascending(),
            # 16
            f"What is the {'7th' if seventh else ''} chord of the scale of {key}?":lambda : chord,
            f"In which scales does this chord appear: {', '.join(chord)}?" : lambda : util.find_scales_of_chord(chord),

            }

    if i is not False:
        return list(questions.items())[i]

    return random.choice(list(questions.items()))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        multiple_questions(int(sys.argv[1]))
    ask()


