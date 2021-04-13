#!/usr/bin/env python3

import common
import random


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))
    
    global possibles
    possibles = set()


def best_sol(attempt):
    """ Desc """
    global solution
    global possibles    
        
    count = 0
    solution_modif = solution
    for solution_tmp in possibles:
        possibles_tmp = possibles.copy()
        nbr_possibles = common.nombre_possibles(possibles_tmp, attempt, solution_tmp)
        if nbr_possibles > count:
            count = nbr_possibles
            solution_modif = solution_tmp
    solution = solution_modif


def best_sol_ini(attempt):
    """ Desc """
    global possibles
    global solution
    nb_different_colors = len(set(common.COLORS) - set(attempt))
    if nb_different_colors >= 6:
        # Il n'y a que deux couleurs différentes dans attempt
        eval = (0,0)
    else:
        # Il y a au moins trois couleurs différentes dans attempt
        eval = (0,1)
    possibles = common.donner_possibles(attempt, eval)
    solution = random.sample(possibles,1)[0]
    return eval

    
def codemaker(attempt):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument) en utilisant la fonction evaluation du fichier common
    """
    global solution
    global possibles
    if possibles == set():
        possibles = common.creer_possibles()
        best_sol(attempt)
        eval = common.evaluation(attempt,solution)
        common.maj_possibles(possibles, attempt, eval)
        return eval
    else:
        best_sol(attempt)
        eval = common.evaluation(attempt, solution)
        common.maj_possibles(possibles, attempt, eval)
        return eval


## A supprimer apres

def test():
    attempt = "RRVV"
    print(attempt)
    global possibles
    global solution
    possibles = creer_possibles()
    best_sol(attempt)
    eval = common.evaluation(attempt, solution)
    possibles = common.donner_possibles(attempt,eval)
    print(len(possibles))
    print(solution, eval)
    # part 2
    print('==='*20)
    possibles = common.donner_possibles(attempt, (0,1))
    solution = random.sample(possibles,1)[0]
    print(len(possibles))
    print(solution)
    
def creer_possibles():
    """ Fonction qui nous donne toutes les possibilités de chaîne de taille LENGTH 
    parmis les couleurs COLORS. """
    count = 0
    set1 = set(common.COLORS)
    while count < common.LENGTH-1:
        set2 = set1.copy()
        for e in set2:
            for e2 in common.COLORS:
                set1.add(e+e2)
        count += 1
        set1 = set1 - set2
    return set1