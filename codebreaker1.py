#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports des fichiers utilisés :
import common

def init():
    """ Fonction qui initialise certains paramètres et variables utiles par la suite """
    global tried_combinations
    tried_combinations = []

def codebreaker(evaluation_p):
    """ Fonction qui renvoie une combinaison au hasard, tant qu'elle ne se trouve pas dans la liste des combinaisons déjà envoyées """
    global tried_combinations
    while True: # Boucle infinie
        attempt = ''.join(common.choices(common.COLORS, common.LENGTH)) # Combinaison au hasard
        if attempt not in tried_combinations:
            tried_combinations.append(attempt)
            return attempt