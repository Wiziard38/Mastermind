#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports des fichiers utilisés :
import common

def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))
    # Pour une version encore plus triviale, on pourrait aussi utiliser solution = ''.join([common.COLORS[0] for i in range(common.LENGTH)])


def codemaker(attempt):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument) en utilisant la fonction evaluation du fichier common
    """
    global solution
    return common.evaluation(attempt, solution)