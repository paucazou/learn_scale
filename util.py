#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

import itertools
import mingus.core.keys as keys
import mingus.core.scales as scales
import random
import string
functions = """tonic
supertonic
mediant
subdominant
dominant
submediant
leadingtone
""".split()

def get_random_key():
    """Get a random key, major or minor"""
    tonics = string.ascii_lowercase[:7]
    tonics = tonics + tonics.upper()
    tonics = itertools.chain.from_iterable([(n,n+'b',n+'#') for n in tonics])
    return random.choice(list(tonics))

def get_scale(key):
    """Return a scale, major or minor,
    matching with key"""
    return scales.Major(key) if key.isupper() else scales.HarmonicMinor(key.upper())

def get_accidentals(key):
    """Return every note with accidental
    in key"""
    scale = get_scale(key)
    return [n for n in scale.ascending() if ('b' in n or '#' in n)]

def get_minor_accidentals(key):
    """Return the sixth and seventh degrees
    augmented in minor scale key"""
    scale = scales.MelodicMinor(key)
    return scale.degree(6), scale.degree(7)

def get_degree_of(key,note):
    """Get the degree of note
    in key"""
    scale = get_scale(key)
    return scale.ascending().index(note)


def find_degree(key,*d):
    """Find the degrees of the scale of the key
    d is a sequence of integer from 1 to 7
    """
    scale = get_scale(key)
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
    return find_degree(scale,*[functions.index(n)+1 for n in f])


