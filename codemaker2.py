#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import random
# Imports des fichiers utilisés :
import common

def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''
    
    global possibles
    possibles = common.creer_possibles()


def best_sol(attempt):
    """ Desc """
    global solution
    global possibles    
        
    count = 0
    for solution_tmp in (possibles-{attempt}):
        possibles_tmp = possibles.copy()
        nbr_possibles = common.nombre_possibles(possibles_tmp, attempt, solution_tmp)
        if nbr_possibles > count:
            count = nbr_possibles
            solution = solution_tmp

    
def codemaker(attempt):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument) en utilisant la fonction evaluation du fichier common
    """
    global solution
    global possibles
    
    best_sol(attempt)
    eval = common.evaluation(attempt,solution)
    common.maj_possibles(possibles, attempt, eval)
    return eval