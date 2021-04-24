#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports des fichiers utilisés :
import common

def init():
    """ Fonction qui initialise certains paramètres et variables utiles par la suite. """
    global solution # Variable comprenant la solution pour une partie donnée
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))


def codemaker(attempt):
    """ Cette fonction evalue la combinaison proposée par le codebreaker (donnée en argument) en utilisant 
    la fonction evaluation du fichier common.py """
    global solution
    return common.evaluation(attempt, solution) # On appelle notre fonction du fichier common qui évalue correctement en fonction de la solution