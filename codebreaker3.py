import common
import numpy
import random

def init():
   global combinaisons
   combinaisons = common.creer_possibles()
   global possibles
   possibles = common.creer_possibles()
   global attempt
   attempt = ''


def best_attempt():
    global combinaisons
    global possibles
    global attempt
    
    count = len(possibles)
    attempt_modif = attempt
    
    for solution_tmp in possibles:
        for attempt_tmp in combinaisons:
            possibles_tmp = possibles.copy()
            nbr_possibles = common.nombre_possibles(possibles_tmp, attempt_tmp, solution_tmp)
            if nbr_possibles < count: 
                # On cherche la combinaison qui donne le moins possible de possibles
                count = nbr_possibles
                attempt_modif = attempt_tmp
    attempt = attempt_modif


def codebreaker(evaluation_p):
    """ Desc """
    global possibles
    global attempt
    global combinaisons
    
    if evaluation_p == None:
        best_attempt()
        return attempt
    elif possibles == set():
        possibles = common.donner_possibles(attempt,evaluation_p)
        attempt = random.sample(possibles,1)[0]
        return attempt
    else:
        common.maj_possibles(possibles, attempt, evaluation_p)
        attempt = random.sample(possibles,1)[0]
        return attempt


def test():
    attempt = "RRVV"
    print(attempt)
    global possibles
    global solution
    possibles = common.creer_possibles()
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