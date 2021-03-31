import matplotlib.pyplot as plt
import numpy as np
import io
import sys

import play
import common

def recup_print(codemaker,codebreaker):
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


def plot_histogram(n,codemaker,codebreaker):
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
        plt.hist(list, range = (0,5000), bins = 500, density = True, label=str(codebreaker.__name__)) 
    if str(codebreaker.__name__) == 'codebreaker2':
        plt.hist(list, range = (0,30), bins = 30, density = True, label=str(codebreaker.__name__)) 

def plot_proba_codebreaker0():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker0 trouve le code"""
    p = 1/(len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,20000,20000)
    def f(x):
        return p*(1-p)**(x-1)
    proba = f(x)
    plt.plot(x, proba, label = "codebreaker0 théorique")

def plot_proba_codebreaker1():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker1 trouve le code"""
    p = 1/(len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,4096,4096)
    proba = [p]*4096
    plt.plot(x, proba, label = "codebreaker1 théorique")

if __name__ == "__main__":
    import codemaker1
    import codebreaker0
    import codebreaker1
    import codebreaker2
    # plot_histogram(100,codemaker1,codebreaker0)
    # plot_histogram(100,codemaker1,codebreaker1)
    plot_histogram(100,codemaker1,codebreaker2)
    # plot_proba_codebreaker0()
    # plot_proba_codebreaker1()
    plt.legend()
    plt.show()