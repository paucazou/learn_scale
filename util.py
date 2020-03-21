#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

import mingus.core.chords as chords
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
degrees = "I II III IV V VI VII".split()

def randbool() -> bool:
    return bool(random.randrange(2))

def get_random_key():
    """Get a random key, major or minor"""
    return random.choice(keys.major_keys + keys.minor_keys)

def get_scale(key,minor=scales.HarmonicMinor):
    """Return a scale, major or minor,
    matching with key"""
    return scales.Major(key) if key[0].isupper() else minor(key.upper())

def get_accidentals(key):
    """Return every note with accidental
    in key"""
    scale = get_scale(key,scales.NaturalMinor)
    return [n for n in scale.ascending() if ('b' in n or '#' in n)]

def get_accidentals_number(key):
    """Return the number of accidentals that can be found at the key
    """
    return len(set(get_accidentals(key)))

def get_minor_accidentals(key):
    """Return the sixth and seventh degrees
    augmented in minor scale key"""
    scale = scales.MelodicMinor(key)
    return scale.degree(6), scale.degree(7)

def get_degree_of(key,note):
    """Get the degree of note
    in key"""
    scale = get_scale(key)
    return scale.ascending().index(note) + 1

def get_relative(key):
    """Get the relative key of key"""
    return keys.relative_minor(key) if key[0].isupper() else keys.relative_major(key)

def get_parallel(key):
    """Get the parallel of key"""
    new_key = f"{key[0].upper() if key[0].islower() else key[0].lower()}{key[1:]}"
    return get_scale(new_key)

def determine_note_scale(note):
    """Determine to which scale this note
    can belong. For minor scales, the seventh degree only
    has two notes"""
    result = []
    for s in scales.determine([note]):
        if "harmonic minor" in s or "natural minor" in s:
            result.append(s.split()[0].lower())
        elif "major" in s and "harmonic" not in s:
            result.append(s.split()[0])

    return set(result)


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

def find_function_chord(key,f):
    """Find the chord of function f
    in key"""
    # for compatibility with mingus
    if f == "leadingtone":
        f = "subtonic"

    return getattr(chords,f)(key)

def find_scales_of_chord(chord):
    """Return every scale in which chord appears"""
    return [n for n in keys.major_keys + keys.minor_keys if not set(chord).difference(set(get_scale(n).ascending()))]

def build_chord(key,degree,seventh=False):
    """Return the chord of the degree in the
    scale of key.
    If seventh is True, return the seventh
    Degree can actually be a function or a roman numeral,
    from I to VII in uppercase
    """
    degree = "subtonic" if degree == "leadingtone" else degree
    method = degree + "7" if seventh else degree
    return getattr(chords,method)(key)

def build_diminished_chord(key):
    """Return the diminished chord of the scale of key"""
    if key[0].isupper():
        return chords.VII(key)
    return chords.II(key)

def build_augmented_chord(key):
    """Return the augmented chord of the scale of key"""
    if key[0].isupper():
        return ""
    key = key[0].upper() + key[1:]
    scale = scales.MelodicMinor(key)
    return chords.augmented_triad(scale.degree(3))




