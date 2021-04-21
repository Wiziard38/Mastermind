#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import numpy as np
import random
import itertools
# Imports des fichiers utilisés :
import common

def init():
    """ Desc """
    global combinaisons
    combinaisons = common.creer_possibles()

    global possibles
    possibles = set()

    global attempt
    attempt = ''

    global tab_evals
    tab_evals = array_evals()


def attempt_to_number(attempt):
    base = len(common.COLORS)
    number = 0
    for (i,v) in enumerate(attempt):
        number += (base**i) * common.COLORS.index(v)
    return number


def array_evals():
    global combinaisons
    size = len(combinaisons)
    matrix = np.array([[[-1,-1]]*size]*size)

    for attempt_tmp, solution_tmp in itertools.product(combinaisons, combinaisons):
        x = attempt_to_number(attempt_tmp)
        y = attempt_to_number(solution_tmp)
        matrix[x][y] = list(common.evaluation(attempt_tmp, solution_tmp))
        #y = list(map(lambda x : list(common.evaluation('RRR', x)), list(combinaisons)))
    return matrix


def best_attempt():
    """ Fonction qui, avec en paramètres la liste des combinaisons encore possibles
    au vu des évaluations précedentes (variable globale) va renvoyer quel est le meilleur
    choix de combinaison possible (dans le pire des cas) """
    global combinaisons
    global possibles
    global attempt
    global tab_evals

    count_1 = len(possibles)
    attempt_modif = attempt

    for attempt_tmp in combinaisons:

        count_0 = 0
        for solution_tmp in possibles:
            possibles_tmp = possibles.copy()

            x = attempt_to_number(attempt_tmp)
            y = attempt_to_number(solution_tmp)

            eval_tmp = tuple(tab_evals[x][y])

            common.maj_possibles(possibles_tmp, attempt_tmp, eval_tmp)
            nbr_possibles = len(possibles_tmp)
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