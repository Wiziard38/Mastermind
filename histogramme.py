import random
import matplotlib.pyplot as plt
import numpy as np
import io
import sys

import codebreaker0
import codemaker0
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

def recup_print():
    # rediriger stdout dans un buffer :
    sys.stdout = io.StringIO()
    # appel de la fonction qui remplira stdout (donc le buffer)
    play(codemaker0, codebreaker0)
    # récupérer le contenu du buffer :
    s = sys.stdout.getvalue()    
    # fermer le buffer :
    sys.stdout.close()    
    # rediriger stdout vers la sortie standart :
    sys.stdout = sys.__stdout__
    s = s[-15:]
    nombre = ''
    for e in s:
        if e.isdigit():
            nombre += str(e)
    return nombre


def histogramme(n):
    list = []
    for i in range(n):
        list.append(recup_print())
    plt.hist(list, range = (0,8000), bins = 8000, color='red')
    plt.title("Nombres d'essais") 
    plt.show()



def trace_histo(n):
    list = []
    p = len(common.COLORS)**common.LENGTH
    for i in range(n):
        proba = True
        nbr_essais = 0
        while proba:
            if random.randint(0,p) == 0:
                list.append(nbr_essais)
                proba = False
            nbr_essais +=1
    plt.hist(list, range = (0,8000), bins = 8000, color='red')
    plt.title("Nombres d'essais") 
    plt.show()
    

def trace_histo2(n): # methode exacte
    p = len(common.COLORS)**common.LENGTH
    list2 = np.random.geometric(1/p, n)
    plt.hist(list2, range = (0,8000), bins = 8000, color='yellow')
    plt.title("Nombres d'essais") 
    plt.show()
