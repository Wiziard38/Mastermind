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
        

def best_attempt():
    """ Fonction qui, avec en paramètres la liste des combinaisons encore possibles
    au vu des évaluations précedentes (variable globale) va renvoyer quel est le meilleur
    choix de combinaison possible (dans le pire des cas) """
    global combinaisons
    global possibles
    global attempt
    
    count_1 = len(possibles)
    attempt_modif = attempt

    for attempt_tmp in combinaisons:
        
        count_0 = 0
        for solution_tmp in possibles:
            possibles_tmp = possibles.copy()
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
        if len(possibles) == 1:
            return list(possibles)[0]
        best_attempt()
        return attempt