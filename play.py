#!/usr/bin/env python3
import os
#os.chdir("/Users/mathis/Desktop/Mastermind")

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

##question 11: fonction play_log
def play_log(codemaker, codebreaker):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    """
    #on reprend la fonction play, on veut ajouter les attempts et les
    #évaluations dans un fichier texte
    
    #on crée un fichier texte log, que l'on ouvre en écriture et lecture (w+)
    log= open("log.txt","w+") 
    
    n_tries = 0
    codebreaker.init()
    codemaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        #on écrit l'attempt dans le log puis on passe à la ligne suivante avec \n
        log.write(attempt+"\n")
        
        (red, white) = codemaker.codemaker(attempt)
        #idem pour l'évaluation retournée par codemaker
        log.write(str(red)+','+str(white)+'\n')
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        
        evaluation_p = (red, white)
        
        if red >= common.LENGTH:
            print("Bravo ! Trouvé {} en {} essais".format(attempt, n_tries))
            break
##fin de la question 11
        
if __name__ == "__main__":
    None
    ##
    import codebreaker2
    import codemaker1
    play(codemaker1, codebreaker2)

    ##
    #  Faire jouer un humain contre codemaker0.py :
    import codemaker1
    play_human_against_codemaker(codemaker1)
    
    ##
    # Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
    import codemaker2
    play_human_against_codemaker(codemaker2)
    
    ##
    import codebreaker2
    import codemaker2
    play(codemaker2, codebreaker2)
