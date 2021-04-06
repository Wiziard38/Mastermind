import common
import numpy
import random

def init():
   global possibles
   possibles = set()
   global attempt
   attempt = ''


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

def best_attempt():
    global possibles
    global attempt
    
    def nombre_possibles(possibles_tmp, attempt, solution_tmp):
        eval_tmp = common.evaluation(attempt, solution_tmp)
        common.maj_possibles(possibles_tmp, attempt, eval_tmp)
        return len(possibles_tmp)
    
    count = len(possibles)
    attempt modif = attempt
    
    for solution_tmp in possibles:
        for attempt_tmp in possibles:
            possibles_tmp = possibles.copy()
            nbr_possibles = nombre_possibles(possibles_tmp, attempt_tmp, solution_tmp)
            if nbr_possibles < count: 
                # On cherche la combinaison qui donne le moins possible de possibles
                count = nbr_possibles
                attempt_modif = attempt_tmp
    attempt = attempt_modif


def codebreaker(evaluation_p):
    """ Desc """
    global possibles
    global attempt
    if evaluation_p == None:
        attempt = ''.join(common.choices(common.COLORS, common.LENGTH))
        return attempt
    elif possibles == set():
        possibles = common.donner_possibles(attempt,evaluation_p)
        best_attempt()
        return attempt
    else:
        common.maj_possibles(possibles, attempt, evaluation_p)
        best_attempt()
        return attempt


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