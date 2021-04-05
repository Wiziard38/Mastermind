import matplotlib.pyplot as plt
import numpy as np
import io
import sys

import common
import play

def recup_print(codemaker, codebreaker):
    """ Fonction qui permet de récuperer du texte qui a été écrit dans la console 
    python par la fonction play appliquée à codebreaker et codemaker"""
    # rediriger stdout dans un buffer :
    sys.stdout = io.StringIO()
    # appel de la fonction qui remplira stdout (donc le buffer)
    play.play(codemaker,codebreaker)
    # récupérer le contenu du buffer :
    s = sys.stdout.getvalue()    
    # fermer le buffer :
    sys.stdout.close()    
    # rediriger stdout vers la sortie standart :
    sys.stdout = sys.__stdout__
    
    # Maintenant on récupère la partie de l'affichage qui nous intéresse :
    s = s[-15:]
    nombre = ''
    for e in s:
        if e.isdigit():
            nombre += str(e)
    return int(nombre)


def plot_histogram(n, codemaker, codebreaker):
    """ Fonction qui trace un histogramme répertoriant le nombre d'essais nécessaires
    pour que codemaker arrive à trouver la combinaison, sur n parties"""
    # On créé la liste du nombre d'essais pour les n parties : 
    list = []
    for i in range(n):
        list.append(recup_print(codemaker, codebreaker))
    # On trace l'histogramme :
    if str(codebreaker.__name__) == 'codebreaker0':
        plt.hist(list, range = (0,20000), bins = 400, density = True, label=str(codebreaker.__name__))  
    if str(codebreaker.__name__) == 'codebreaker1':
        plt.hist(list, range = (0,4500), bins = 90, density = True, label=str(codebreaker.__name__)) 
    if str(codebreaker.__name__) == 'codebreaker2':
        plt.hist(list, range = (0,30), bins = 30, density = True, label=str(codebreaker.__name__)) 

def plot_difference_codebreakers(n, codemaker, codebreaker_1, codebreaker_2):
    """ Fonction qui trace un histogramme répertoriant la différence du nombre 
    d'essais sur n parties nécessaires, pour que codemaker arrive à trouver la 
    combinaison pour deux versions de codebreakers."""
    # On créé la liste de la différence du nombre d'essais pour les n parties : 
    list = []
    for i in range(n):
        list.append(recup_print(codemaker, codebreaker_1) - recup_print(codemaker, codebreaker_2))
        
    # On trace l'histogramme :
    text = "diffence du nombre d'essais entre " + str(codebreaker_1.__name__) + " et " + str(codebreaker_2.__name__)
    plt.hist(list, range = (-1000,20000), bins = 420, density = True, label=text) 

def plot_difference_codemakers(n, codemaker_1, codemaker_2, codebreaker):
    """ Fonction qui trace un histogramme répertoriant la différence du nombre 
    d'essais sur n parties nécessaires, pour deux versions de codemakers différentes
    arrivent à trouver la combinaison."""
    # On créé la liste de la différence du nombre d'essais pour les n parties : 
    list = []
    for i in range(n):
        list.append(recup_print(codemaker_1, codebreaker) - recup_print(codemaker_2, codebreaker))
        
    # On trace l'histogramme :
    text = "diffence du nombre d'essais entre " + str(codemaker_1.__name__) + " et " + str(codebmaker_2.__name__)
    plt.hist(list, range = (-1000,20000), bins = 420, density = True, label=text) 
    
    
def plot_proba_codebreaker0():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker0 trouve le code"""
    p = 1/(len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,20000,20000)
    proba = (lambda x: p*(1-p)**(x-1))(x)
    plt.plot(x, proba, label = "codebreaker0 théorique")

def plot_proba_codebreaker1():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker1 trouve le code"""
    p = 1/(len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,4096,4096)
    proba = [p]*4096
    plt.plot(x, proba, label = "codebreaker1 théorique")

# Fonctions de tracé    

if __name__ == "__main__":
    import codemaker1
    import codemaker2
    import codebreaker0
    import codebreaker1
    import codebreaker2
    # plot_histogram(100,codemaker1,codebreaker0)
    #plot_histogram(1000,codemaker1,codebreaker1)
    #plot_histogram(100,codemaker1,codebreaker2)
    #plot_histogram(5,codemaker2,codebreaker2)
    #plot_proba_codebreaker0()
    #plot_proba_codebreaker1()
    plot_difference_codebreakers(100, codemaker1, codebreaker0, codebreaker1)
    #plot_difference_codemakers(100, codemaker1, codemaker2, codebreaker1)
    plt.legend()
    plt.show()