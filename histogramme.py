#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import des librairies utilisées :
import matplotlib.pyplot as plt
import numpy as np
import io
import sys
# Imports des fichiers utilisés :
import common
import play

def recup_print(codemaker, codebreaker):
    """ Fonction qui permet de récuperer du texte qui a été écrit dans la console 
    python par la fonction play appliquée à un codebreaker et un codemaker. """
    # rediriger stdout dans un buffer :
    sys.stdout = io.StringIO()
    # appel de la fonction qui remplira stdout (donc le buffer)
    play.play(codemaker,codebreaker)
    # récupérer le contenu du buffer :
    sortie = sys.stdout.getvalue()    
    # fermer le buffer :
    sys.stdout.close()    
    # rediriger stdout vers la sortie standart :
    sys.stdout = sys.__stdout__
    
    # Maintenant on récupère la partie de l'affichage qui nous intéresse (c'est-à-dire la partie où le nombre d'essais est affichée):
    sortie = sortie[-15:]
    nombre = ''
    for character in sortie:
        if character.isdigit(): # On regarde si chaque caractère est un nombre
            nombre += str(character)
    return int(nombre)


def plot_histogram(n, codemaker, codebreaker):
    """ Fonction qui trace un histogramme répertoriant le nombre d'essais nécessaires
    pour que codemaker arrive à trouver la combinaison, sur n parties"""
    # On créé la liste du nombre d'essais pour les n parties : 
    liste_essais = list(map(lambda x : recup_print(codemaker, codebreaker), np.zeros(n)))
    
    # On trace l'histogramme :
    M = max(liste_essais)
    if str(codebreaker.__name__) == 'codebreaker0':
        plt.hist(liste_essais, range = (0,M+1), bins = int(M/100), density = True, label=str(codebreaker.__name__))
    if str(codebreaker.__name__) == 'codebreaker1':
        p = (len(common.COLORS)**common.LENGTH)
        plt.hist(liste_essais, range = (0,p+1), bins = int(p/32), density = True, label=str(codebreaker.__name__)) 
    if str(codebreaker.__name__) == 'codebreaker2':
        plt.hist(liste_essais, range = (0,M+1), bins = M+1, density = True, label=str(codebreaker.__name__)) 

    # On affiche la moyenne du nombre d'essais par parties
    plt.title("Moyenne du nombre d'essais dans une partie entre {} \n et {} : {}".format(codemaker.__name__, codebreaker.__name__, np.mean(liste_essais)))
    # On nomme les axes 
    plt.xlabel("Nombre d'essais")
    plt.ylabel("Nombre de parties, pondérées")


def plot_difference_codebreakers(n, codemaker, codebreaker_1, codebreaker_2):
    """ Fonction qui trace un histogramme répertoriant la différence du nombre 
    d'essais sur n parties nécessaires, pour que codemaker arrive à trouver la 
    combinaison pour deux versions de codebreakers."""
    # On créé la liste de la différence du nombre d'essais pour les n parties : 
    liste_gains = list(map(lambda x : recup_print(codemaker, codebreaker_1) - recup_print(codemaker, codebreaker_2), np.zeros(n)))
       
    # On trace l'histogramme :
    (M,m) = (max(liste_gains),min(liste_gains))
    text = "différence du nombre d'essais entre {} et {}".format(codebreaker_1.__name__, codebreaker_2.__name__)
    plt.hist(liste_gains, range = (m,M+1), bins = (M+1-m), density = True, label=text) 

    # On affiche la moyenne du nombre d'essais par parties
    plt.title("Moyenne du gain en nombre d'essais dans une partie entre {} \n et {} contre {} : {}".format(codebreaker_1.__name__, codebreaker_2.__name__, codemaker.__name__, np.mean(liste_gains)))
    # On nomme les axes 
    plt.xlabel("Nombre d'essais")
    plt.ylabel("Nombre de parties, pondérées")

def plot_difference_codemakers(n, codemaker_1, codemaker_2, codebreaker):
    """ Fonction qui trace un histogramme répertoriant la différence du nombre 
    d'essais sur n parties, entre deux versions de codemakers différentes. """
    # On créé la liste de la différence du nombre d'essais pour les n parties : 
    liste_gains = list(map(lambda x : recup_print(codemaker_1, codebreaker) - recup_print(codemaker_2, codebreaker), np.zeros(n)))
    
    # On trace l'histogramme :
    (M,m) = (max(liste_gains),min(liste_gains))
    text = "diffence du nombre d'essais entre {} et {}".format(codemaker_1.__name__, codemaker_2.__name__)
    plt.hist(liste_gains, range = (m,M+1), bins = (M+1-m), density = True, label=text) 
    
    # On affiche la moyenne du nombre d'essais par parties
    plt.title("Moyenne du gain en nombre d'essais dans une partie entre {} \n et {} contre {} : {}".format(codemaker_1.__name__, codemaker_2.__name__, codebreaker.__name__, np.mean(liste_gains)))
    # On nomme les axes 
    plt.xlabel("Nombre d'essais")
    plt.ylabel("Nombre de parties, pondérées")

def plot_proba_codebreaker0():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker0 trouve le code"""
    p = (len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,5*p,5*p)
    values = list(map(lambda x : (1/p)*(1-1/p)**(x-1), x))
    plt.plot(x, values, label = "codebreaker0 théorique")

def plot_proba_codebreaker1():
    """ Fonction qui permet de tracer de manière probabilistique le nombre d'essais
    nécessaires pour que codebreaker1 trouve le code"""
    p = (len(common.COLORS)**common.LENGTH)
    x = np.linspace(0,p,p)
    values = [1/p]*p
    plt.plot(x, values, label = "codebreaker1 théorique")


# Fonctions de tracé    

if __name__ == "__main__":
    import codemaker1
    import codemaker2
    import codebreaker0
    import codebreaker1
    import codebreaker2
    plot_histogram(100,codemaker1,codebreaker0)
    #plot_histogram(5000,codemaker1,codebreaker1)
    #plot_histogram(10,codemaker2,codebreaker2)
    #plot_histogram(20,codemaker2,codebreaker2)
    #plot_proba_codebreaker0()
    #plot_proba_codebreaker1()
    #plot_difference_codebreakers(10, codemaker1, codebreaker0, codebreaker1)
    #plot_difference_codemakers(10, codemaker1, codemaker2, codebreaker1)
    plt.legend()
    plt.show()