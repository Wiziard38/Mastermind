#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports des fichiers utilisés :
import common

def init():
    """ Fonction qui initialise certains paramètres et variables utiles par la suite """
    global solution # Variable comprenant la solution pour une partie donnée, mais qui pourra être modifiée dans ce programme
    solution = ''
    global possibles # Variable qui contiendra l'ensemble des combinaisons possibles
    possibles = common.creer_possibles()


def best_sol(attempt):
    """ Fonction qui, avec en paramètre l'essai à un tour donné, et en variable globale l'ensemble des possibles, va associer à la
    variable solution la solution telle que la liste des possibles une fois cette solution choisie soit la plus longue possibles. """
    global solution
    global possibles    
        
    count = 0 # Compteur qui contiendra le nombre de possibles après mise-à-jour
    for solution_tmp in (possibles-{attempt}): # On essaye toutes les solutions sauf celle proposée comme attempt, qui ne pourra jamais être la meilleure
        # On compte le nombre de combinaisons possibles après mise à jour avec un attempt et solution donnés
        possibles_tmp = possibles.copy()
        nbr_possibles = common.nombre_possibles(possibles_tmp, attempt, solution_tmp)
        if nbr_possibles > count: # Si pour une solution donnée le nombre de possibles et plus grand que celui en mémoire :
            count = nbr_possibles # On modifie le compteur
            solution = solution_tmp # Notre solution prend pour valeur cette solution donnée

    
def codemaker(attempt):
    """ Cette fonction évalue la combinaison proposée par le codebreaker (donnée en argument) en utilisant la fonction evaluation 
    du fichier common.py. Mais en plus, la fonction vient choisir une solution parmis celles qui sont encore possibles (c'est-à-dire 
    qui respenctent toutes les évaluations), telle que en utilisant cette solution le programme renvoie le moins d'informations possibles."""
    global solution
    global possibles
    best_sol(attempt) # On vient appeler cette fonction pour choisir la meilleure solution
    eval = common.evaluation(attempt,solution)
    common.maj_possibles(possibles, attempt, eval)
    return eval