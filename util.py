#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

import itertools
import mingus.core.keys as keys
import mingus.core.scales as scales
import random
import string

def get_random_key():
    """Get a random key, major or minor"""
    tonics = string.ascii_lowercase[:7]
    tonics = tonics + tonics.upper()
    tonics = itertools.chain.from_iterable([(n,n+'b',n+'#') for n in tonics])
    return random.choice(list(tonics))

def find_degree(key,*d):
    """Find the degrees of the scale of the key
    d is a sequence of integer from 1 to 7
    """
    scale = scales.Major(key) if key.isupper() else scales.HarmonicMinor(key.upper())
    return [scale.degree(i) for i in d]

def find_function(scale,*f):
    """Find the function of functions f in scale
    and return matching notes.
    Name of functions:
        - tonic
        - supertonic
        - mediant
        - subdominant
        - dominant
        - submediant
        - leadingtone
        """
    functions = """none
    tonic
    supertonic
    mediant
    subdominant
    dominant
    submediant
    leadingtone
    """.split()
    return find_degree(scale,*[functions.index(n) for n in f])


