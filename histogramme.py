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
    plt.hist(list, range = (0,20000), bins = 400, density = True)
    plt.title("Nombre d'essais de " + codebreaker.__name__ + " pour un total de " +str(n)+ " parties") 
    plt.show()
    
    # Loi géomérique (courbe exacte) :
    p = 1/(len(common.COLORS)**common.LENGTH) # On définit la probabilité de trouver à chaque essais
    x = np.linspace(0,20000,20000)
    def f(x):
        return p*(1-p)**(x-1)
    proba = f(x)
    plt.plot(x, proba)


def plot_histogram_exact(n):
    """Fonction qui trace l'histogramme représentatif du nombre d'essais par parties
    jouées (en terme de probabilités) """
    p = 1/(len(common.COLORS)**common.LENGTH) # On définit la probabilité de trouver à chaque essais
    
    # Loi géomérique (histogramme) :
    list = np.random.geometric(p,n)
    return plt.hist(list, range = (0,20000), bins = 400, color='red', density = True)
    plt.title("Nombre d'essais probables moyens pour un total de " +str(n)+ " parties") 
    

def trace_proba_codebreaker0():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker0 trouve le code"""
    p = 1/(len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,20000,20000)
    def f(x):
        return p*(1-p)**(x-1)
    proba = f(x)
    return plt.plot(x, proba)

def trace_proba_codebreaker1():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker1 trouve le code"""
    p = 1/(len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,4096,4096)
    proba = [p]*4096
    return plt.plot(x,proba)

if __name__ == "__main__":
    None
    ##
    import codemaker0
    import codebreaker0
    plot_histogram(100000,codemaker0,codebreaker0)