#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Contains the class representing a scale"""

import string

class Scale:
    __name_notes = string.ascii_lowercase[:7]
    def __init__(self,name:str):
        """Creates a scale based on the input.
        The input is the tonic. If major, the tonic is
        upper case; if minor, lower case.
        Sharp or flat can be indicated in lower case,
        just after the name of the tonic. No double sharp, flat,
        and no normal is allowed.
        Examples:
            - A (A major)
            - b (B minor)
            - db (D flat minor)
            - Fs (F sharp major)
            """
        # checks
        assert len(name) in (1,2)
        assert name[0].lower() in self.__name_notes
        if len(name) == 2:
            assert name[1] in 'b#'
        
        # creation
        self.tonic = self.__name_notes.find(name[0].lower())
        self.alteration = "" if len(name) == 1 else name[1]
        self.mode = "M" if name[0].isupper() else "m"

    def _generate_scale(self):
        """Generates a scale based on the information given"""

        self.notes = self.__name_notes[:self.tonic] + self.__name_notes[self.tonic:]

