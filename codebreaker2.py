#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import random
# Imports des fichiers utilisés :
import common

def init():
    """ Fonction qui initialise certains paramètres et variables utiles par la suite """
    global possibles # Variable qui contiendra l'ensemble des combinaisons possibles
    possibles = set()
    global attempt # Variable qui contiendra l'essai proposé, utilisé du coup au tour d'après
    attempt = ''

def codebreaker(evaluation_p):
    """ Fonction qui va renvoyer un attempt au hasard, tant que celui-ci se trouve dans la liste des 
    combinaisons encore possibles au vu des évaluations précedentes. C'est-à-dire, tant que cet attempt 
    respecte toutes les précédentes évaluations. """
    global possibles
    global attempt
    if evaluation_p == None: # Correspond au premier essai
        attempt = ''.join(common.choices(common.COLORS, common.LENGTH)) # On choisit un au hasard parmis toutes les combinaisons
        return attempt
    elif possibles == set(): # Correspond au deuxième essai
        possibles = common.donner_possibles(attempt,evaluation_p) 
        attempt = random.sample(possibles,1)[0] # On choisit un au hasard parmis les possibles
        return attempt
    else: # Correspond à tous les autres essais
        common.maj_possibles(possibles, attempt, evaluation_p)
        attempt = random.sample(possibles,1)[0] # On choisit un au hasard parmis les possibles
        return attempt