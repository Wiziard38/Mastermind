#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import sys
import numpy as np
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


## Programme du codemaker3 avec de la programmation dynamique   
def init():
    """ Fonction qui initialise certains paramètres et variables utiles par la suite """
    global combinaisons # Variable qui contient toutes les combinaisons
    combinaisons = common.creer_possibles()

    global possibles # Variable qui contiendra l'ensemble des combinaisons possibles
    possibles = common.creer_possibles()

    global attempt # Variable qui contiendra l'essai proposé, utilisé du coup au tour d'après
    attempt = ''

    global tab_evals # Variable qui contiendra un tableau comprenant toutes les évaluations possibles.
    size = len(common.COLORS)**common.LENGTH
    tab_evals = np.array([[[-1,-1]]*size]*size)


def attempt_to_number(attempt):
    """ Programme qui permet d'assogner une valeur entière à un attempt donné.
    Cette valeur sera différente chaque combinaison de couleurs. 
    Le but est de pouvoir stocker et retrouver une évaluation epour chaque combinaisons dans un tableau. """
    base = len(common.COLORS) # On introduit une base pour notre calcul
    number = 0
    for (i,v) in enumerate(attempt): # On transforme notre attempt en cette base grâce à la valeur (position) de chaque couleur dans la chaîne des couleurs.
        number += (base**i) * common.COLORS.index(v) 
    return number


def best_attempt():
    """ Fonction qui, avec en paramètres la liste des combinaisons encore possibles
    au vu des évaluations précedentes (variable globale) va renvoyer quel est le meilleur
    choix de combinaison possible (dans le pire des cas). """
    global combinaisons
    global possibles
    global attempt
    global tab_evals

    count_1 = len(possibles) # Compteur des minimums

    for attempt_tmp in combinaisons: # On parcourt tous les attempts parmis les combinaisons possibles
        count_0 = 0 # Compteur des maxs

        for solution_tmp in possibles: # On parcourt les solutions qui sont encore possibles
            # On va calculer le nombre de combinaisons possibles après mise à jour pour un attempt et une solution donnés :
            possibles_tmp = possibles.copy()
            x = attempt_to_number(attempt_tmp)
            y = attempt_to_number(solution_tmp)
            # On regarde si notre évaluation est déjà présente dans le tableau
            if tab_evals[x][y][0] == -1: # Si la valeur n'est pas présente, on calcule l'évaluation et on la stocke
                eval_tmp = common.evaluation(attempt_tmp, solution_tmp)
                tab_evals[x][y] = list(eval_tmp)
            else: # Si la valeur est déjà présente, on la récupère
                eval_tmp = tuple(tab_evals[x][y])

            common.maj_possibles(possibles_tmp, attempt_tmp, eval_tmp)
            nbr_possibles = len(possibles_tmp)
            count_0 = max(count_0, nbr_possibles) # On prend le max entre notre compteur, qui sert de mémoire, et le nombre de combinaisons calculées.

        if count_0 < count_1: 
            # On prend le minimum entre notre compteur et le max du nombre de combinaisons possibles pour un attempt donné.
            count_1 = count_0
            attempt = attempt_tmp


def codebreaker(evaluation_p):
    """ Fonction qui va, à chaque tour, évaluer quel est l'attempt, parmis toutes les combinaisons, 
    qui lui fournira le plus d'informations dans le pire des cas. """
    global possibles
    global attempt
    global combinaisons
    if evaluation_p == None: # Correspond au premier essais 
        best_attempt()
        return attempt
    else: # Correspond à tous les autres essais
        common.maj_possibles(possibles, attempt, evaluation_p)
        if len(possibles) == 1: # Dans le cas où il reste plus qu'une combinaison, il n'y a plus qu'à essayer celle-là qui sera la solution !
            return list(possibles)[0]
        best_attempt()
        return attempt