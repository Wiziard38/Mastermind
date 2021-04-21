#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import os
# Imports des fichiers utilisés :
import common

def check_codemaker(file):
    path = os.getcwd()
    with open(path + "/logs/" + file + ".txt", "r") as log:
        # Initialisation :
        attempt =log.readline().strip()
        (red,white) = log.readline().strip().split(',')
        eval = (int(red),int(white))
        possibles = common.donner_possibles(attempt, eval)        
        while eval != (common.LENGTH,0):
            attempt =log.readline().strip()
            (red,white) = log.readline().strip().split(',')
            eval = (int(red),int(white))
            common.maj_possibles(possibles, attempt, eval)
    if len(possibles) == 0:
        print('Le programme a triché de manière visible !')
    else:
        print("Tout va bien, le codemaker n'a pas triché (de manière visible).")

check_codemaker('log')