#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import numpy as np
import random
import sys
# Imports des fichiers utilisés :
import common


## Fonction evaluation en utilisant des listes de compréhension
def evaluation_v2(attempt, solution):
    """Fonction qui évalue un essai en fonction de la solution de référence.
    Renvoie un tuple composé du nombre de plots de la bonne couleur bien placés,
    et du nombre de plots de la bonne couleur mais mals placés.
    """
    if len(solution) != len(attempt): # On vérifie que les deux chaînes ont la même longueur
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")

    (red, white) = (0,0) # Nombre de plots bien placés, mal placés
    list_attempt = ['*' if attempt[i] == solution[i] else attempt[i] for i in range(common.LENGTH)]
    # On créé une liste qui pour pour tout i allant de 0 à LENGTH vaut '*' si le plot était bien placé, et attempt[i] sinon
    list_solution = ['#' if list_attempt[i] == '*' else solution[i] for i in range(common.LENGTH)]
    # On créé de la même sorte une liste qui pour tout i allant de 0 à LENGTH vaut '#' si attempt[i] valait '*', et solution[i] sinon
    red = list_attempt.count('*') # On compte le nombre de plots bien placés en relevant le nombre de '*'

    for element in list_attempt:
        if element != '*' and element in list_solution: # On prend en compte que les plots mal placés
            white += 1
            list_solution[list_solution.index(element)] = '#'
    return (red, white)


## Programme du codemaker3 utilisant de la programmation dynamique
def init():
    """ Desc """
    global combinaisons
    combinaisons = common.creer_possibles()

    global possibles
    possibles = set()

    global attempt
    attempt = ''

    global tab_evals
    size = len(common.COLORS)**common.LENGTH
    tab_evals = np.array([[[-1,-1]]*size]*size)


def attempt_to_number(attempt):
    base = len(common.COLORS)
    number = 0
    for (i,v) in enumerate(attempt):
        number += (base**i) * common.COLORS.index(v)
    return number


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

            if tab_evals[x][y][0] == -1:
                eval_tmp = common.evaluation(attempt_tmp, solution_tmp)
                tab_evals[x][y] = list(eval_tmp)
            else:
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