#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import os
# Imports des fichiers utilisés :
import common

def play(codemaker, codebreaker):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    """
    n_tries = 0
    codebreaker.init()
    codemaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Bravo ! Trouvé {} en {} essais".format(attempt, n_tries))
            break


def play_human_against_codemaker(codemaker):
    """
    Fait jouer l'utilisateur humain (au clavier) dans le role du codebreaker
    contre un codemaker donné en argument
    """
    n_tries = 0
    codemaker.init()
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = input("Saisir combinaison: ")  # On lit une combinaison au clavier au lieu d'appeler le codebreaker (qui sera donc joué par un humain)
        if len(attempt) != 4:
            print("Combinaison invalide (pas la bonne taille)")
            continue
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        if red >= common.LENGTH:
            print("Bravo ! Trouvé {} en {} essais".format(attempt, n_tries))
            break


def play_human_against_codebreaker(codebreaker):
    """
    Fait jouer l'utilisateur humain (au clavier) dans le role du codemaker
    contre un codebreaker donné en argument
    """
    n_tries = 0
    codebreaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        print('Combinaison proposée: {}'.format(attempt))
        red = int(input('Saisir nombre de plots rouges: '))
        white = int(input('Saisir nombre de plots blancs: '))
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Le codebreaker a trouvé {} en {} essais".format(attempt, n_tries))
            break


def play_log(codemaker, codebreaker, file):
    """ Fonction similaire à play, mais qui au lieu de print les différentes informations, cette fonction va
    les stocker dans un fichier, avec le nom pris en paramètre. """
    # On crée un fichier texte log, que l'on ouvre en écriture et lecture (w+)
    path = os.getcwd()
    log = open(path + "/logs/" + file + ".txt", "w+")

    n_tries = 0
    codebreaker.init()
    codemaker.init()
    evaluation_p = None
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        # On écrit l'attempt dans le log puis on passe à la ligne suivante avec \n
        log.write(attempt+"\n")

        (red, white) = codemaker.codemaker(attempt)
        # Idem pour l'évaluation retournée par codemaker
        log.write(str(red)+','+str(white)+'\n')
        n_tries += 1

        evaluation_p = (red, white)
        if red >= common.LENGTH:
            break
    print("La partie a bien été enregistrée dans /logs/" + file + " !")

## Exemples de parties, que vous pouvez décommentez, et bien entendu changer les versions de codemaker et codebreaker
import codemaker1
import codemaker2
import codebreaker0
import codebreaker1
import codebreaker2
import codebreaker3
# play(codemaker1, codebreaker1)
# play_human_against_codemaker(codemaker2)
# play_human_against_codebreaker(codebreaker3)
# play_log(codemaker2, codebreaker2, "log42")