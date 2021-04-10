import common
import numpy
import random

def init():
    """ Desc """
    global combinaisons
    combinaisons = common.creer_possibles()
    global possibles
    possibles = set()
    global attempt
    attempt = ''

# def best_attempt_ini():
#     """ Desc """"
#     global attempt
#     while True:
#         attempt = ''.join(common.choices(common.COLORS, common.LENGTH))
#         if len(set(common.COLORS) - set(attempt)) == common.LENGTH:
#             return attempt

def best_attempt():
    """ Fonction qui, avec en paramètres la liste des combinaisons encore possibles
    au vu des évaluations précedentes (variable globale) va renvoyer quel est le meilleur
    choix de combinaison possible (dans le pire des cas) """
    global combinaisons
    global possibles
    global attempt
    
    count_0 = 0
    count_1 = len(possibles)
    attempt_modif = attempt
        
    for attempt_tmp in combinaisons:
        
        for solution_tmp in possibles:
            possibles_tmp = possibles.copy()
            # common.maj_possibles(possibles_tmp, attempt_tmp)
            nbr_possibles = common.nombre_possibles(possibles_tmp, attempt_tmp, solution_tmp)
            
            count_0 = max(count_0, nbr_possibles)
            
        if count_0 < count_1:
            
            count_1 = count_0
            attempt_modif = attempt_tmp
    attempt = attempt_modif


def codebreaker(evaluation_p):
    """ Desc """
    global possibles
    global attempt
    global combinaisons
    if evaluation_p == None:
        # Correspond au premier essai
        possibles = common.creer_possibles()
        attempt = ''
        best_attempt()
        return attempt
    elif possibles == set():
        # Correspond au deuxième essai
        possibles = common.donner_possibles(attempt,evaluation_p)
        best_attempt()
        return attempt
    else:
        # Correspond à tous les autres essais
        common.maj_possibles(possibles, attempt, evaluation_p)
        best_attempt()
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