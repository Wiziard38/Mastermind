#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import numpy as np
import random
import itertools
# Imports des fichiers utilisés :
import common


def init():
    """ Fonction qui initialise certains paramètres et variables utiles par la suite """
    global combinaisons # Variable qui contient toutes les combinaisons 
    combinaisons = common.creer_possibles()
    global possibles # Variable qui contiendra l'ensemble des combinaisons possibles
    possibles = common.creer_possibles()
    global attempt # Variable qui contiendra l'essai proposé, utilisé du coup au tour d'après
    attempt = ''


def best_attempt():
    """ Fonction qui, avec en paramètres la liste des combinaisons encore possibles
    au vu des évaluations précedentes (variable globale) va renvoyer quel est le meilleur
    choix de combinaison possible (dans le pire des cas) """
    global combinaisons
    global possibles
    global attempt

    count_1 = len(possibles)

    for attempt_tmp in combinaisons:

        count_0 = 0
        for solution_tmp in possibles:
            possibles_tmp = possibles.copy()
            nbr_possibles = common.nombre_possibles(possibles_tmp, attempt_tmp, solution_tmp)
            count_0 = max(count_0, nbr_possibles)
        if count_0 < count_1:
            count_1 = count_0
            attempt = attempt_tmp


def codebreaker(evaluation_p):
    """ Fonction qui va, à chaque tour, évaluer quel est l'attempt, parmis toutes les combinaisons, 
    qui lui fournira le plus d'informations dans le pire des cas. """
    global possibles
    global attempt
    global combinaisons
    if evaluation_p == None: # Correspond au premier essai
        best_attempt()
        return attempt
    else: # Correspond à tous les autres essais
        common.maj_possibles(possibles, attempt, evaluation_p)
        if len(possibles) == 1: 
            return list(possibles)[0]
        best_attempt()
        return attempt