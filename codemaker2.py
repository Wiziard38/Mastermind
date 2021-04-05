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
    # Pour une version encore plus triviale, on pourrait aussi utiliser solution = ''.join([common.COLORS[0] for i in range(common.LENGTH)])


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



def best_sol(attempt):
    
    def nombre_possibles(possibles_tmp, attempt, solution_tmp):
        eval_tmp = common.evaluation(attempt, solution_tmp)
        common.maj_possibles(possibles_tmp, attempt, eval_tmp)
        return len(possibles_tmp)
    
    global solution
    global possibles
    count = 0
    solution_modif = solution
    for solution_tmp in possibles:
        possibles_tmp = possibles.copy()
        nbr_possibles = nombre_possibles(possibles_tmp, attempt, solution_tmp)
        if nbr_possibles > count:
            count = nbr_possibles
            solution_modif = solution_tmp
    solution = solution_modif
    
    
def codemaker(attempt):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument) en utilisant la fonction evaluation du fichier common
    """
    global solution
    global possibles
    if possibles == set():
        # Variante pour un gain de temps considérable, normalement même gain en essais
        # On prend une eval = (0,1), quasi toujours le meilleur
        liste = []
        for e in common.COLORS:
            liste.append(e*common.LENGTH)
        # Car (0,1) impossible pour 'RRRR'
        if attempt not in liste:
            possibles = common.donner_possibles(attempt, (0,1))
            solution = random.sample(possibles,1)[0]
            return (0,1)
        else:
            possibles = common.donner_possibles(attempt, (0,0))
            solution = random.sample(possibles,1)[0]
            return (0,0)
    else:
        best_sol(attempt)
        eval = common.evaluation(attempt, solution)
        common.maj_possibles(possibles, attempt, eval)
        print(len(possibles))
        print(solution)
        return eval


def codemaker_bis(attempt):
    """
    FONCTION BIS NON UTILISEE CAR TROP LENTE SUR LA PREMIERE ITERATION
    """
    global solution
    global possibles
    if possibles == set():
        possibles = creer_possibles()
        best_sol(attempt)
        eval = common.evaluation(attempt, solution)
        possibles = common.donner_possibles(attempt,eval)
        print(len(possibles))
        print(solution)
        return eval
    else:
        best_sol(attempt)
        eval = common.evaluation(attempt, solution)
        common.maj_possibles(possibles, attempt, eval)
        print(len(possibles))
        print(solution)
        return eval



def test():
    attempt = "VMNR"
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