#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import numpy
import random
# Imports des fichiers utilisés :
import common

def init():
    """ Desc """
    global possibles
    possibles = set()
    
    global attempt
    attempt = ''

def codebreaker(evaluation_p):
    """ Desc """
    global possibles
    global attempt
    if evaluation_p == None:
        attempt = ''.join(common.choices(common.COLORS, common.LENGTH))
        return attempt
    elif possibles == set():
        possibles = common.donner_possibles(attempt,evaluation_p)
        attempt = random.sample(possibles,1)[0]
        return attempt
    else:
        common.maj_possibles(possibles, attempt, evaluation_p)
        attempt = random.sample(possibles,1)[0]
        return attempt