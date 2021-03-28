#!/usr/bin/env python3
import os
os.chdir("/Users/mathis/Desktop/Mastermind")
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
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = input("Saisir combinaison: ")  # On lit une combinaison au clavier au lieu d'appeler le codebreaker (qui sera donc joué par un humain)
        if len(attempt) != 4:
            print("Combinaison invalide (pas la bonne taille)")
            continue
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
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

if __name__ == "__main__":
    None
    ##
    import codebreaker1
    import codemaker0
    play(codemaker0, codebreaker1)
    
    ##
    #  Faire jouer un humain contre codemaker0.py :
    import codemaker0
    play_human_against_codemaker(codemaker0)
    
    ##
    # Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
    import codemaker1
    play_human_against_codemaker(codemaker1)
    
    ##
    import codebreaker2
    import codemaker2
    play(codemaker2, codebreaker2)
