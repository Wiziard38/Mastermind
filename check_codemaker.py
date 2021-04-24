#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import os
# Imports des fichiers utilisés :
import common

def check_codemaker(file):
    """ Fonction qui vient va évaluer, pour une partie stockée dans un fichier donné en paramètre, 
    si le codemaker a trché de manière visible ou non pour cette-dite partie. """
    path = os.getcwd()
    with open(path + "/logs/" + file + ".txt", "r") as log:
        # Initialisation pour le premier essai + evaluation associée :
        attempt =log.readline().strip()
        (red,white) = log.readline().strip().split(',')
        eval = (int(red),int(white))
        possibles = common.donner_possibles(attempt, eval) # On va tenir le long du programme une variable qui comorend les combinaisons encore possibles

        while eval != (common.LENGTH,0):
            # On parcourt pour chaque essai + evaluation
            attempt =log.readline().strip()
            (red,white) = log.readline().strip().split(',')
            eval = (int(red),int(white))
            common.maj_possibles(possibles, attempt, eval) # On met à jour notre variable des possibles
    if len(possibles) == 0: # Si aucune combinaison ne correspond à l'ensemble des evaluation renvoyées par codemaker, alors celui-ci a triché
        print('Le programme a triché de manière visible !')
    else: # Dans ce cas, codemaker n'a pas triché
        print("Tout va bien, le codemaker n'a pas triché (de manière visible).")

## Pour exécuter ce programme avec en entrée le fichier 'log' par exemple, décommentez la ligne suivante :
# check_codemaker('log')