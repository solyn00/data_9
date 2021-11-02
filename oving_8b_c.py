# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:47:45 2021

@author: Sondre Lyngstad
"""

from __future__ import annotations

import re
from pathlib import Path


class MultipleChoise:

    def __init__(self, question, alternatives, answer):
        self.question = question
        self.answer = answer
        self.alternatives = alternatives
        

    def __str__(self):
        return f"{self.question}\n" + "\n".join(
            [
                f"    {index + 1}: {alternative}"
                for index, alternative in enumerate(self.alternatives)
            ]
        )

    def sjekk_svar(self, answer):
       return self.answer == int(answer) -1


liste = [
    MultipleChoise(
        question="Hvilken planet er nærmest solen?",
        alternatives=["Mars", "Venus", "Merkur", "Jorden"],
        answer=2
        
    ),
    MultipleChoise(
        question="Hvilket land har størst konsum av sjokolade per innbygger?",
        alternatives=["Amerika", "Sveits", "Norge", "Canada"],
        answer=1
    ),
]
"""for element in liste:
    def ask_qestion():
        print(f"{element}\n")
        answer = input("Svar: ")
        if element.sjekk_svar(answer):
            print("RIKTIG!\n")
        else:
            print("FEIL!\n")
            ask_qestion()
    ask_qestion()"""
