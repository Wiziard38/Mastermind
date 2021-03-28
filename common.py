#!/usr/bin/env python3

import random
import sys

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']


def choices(e, n):
    """Renvoie une liste composée de n éléments tirés de e avec remise
    On pourrait utiliser random.choices, mais cette fonction n'est pas
    disponible dans les versions plus anciennes de Python
    """
    return [random.choice(e) for i in range(n)]

    
def evaluation(solution, attempt):
    """Fonction qui évalue un essai en fonction de la solution de référence.
    Renvoie un tuple composé du nombre de plots de la bonne couleur bien placés, 
    et du nombre de plots de la bonne couleur mais mals placés.
    """
    
    dict = {}
    """On va d'abord compter le nombre de rouges, les couleurs sont soit rouges,
    soit on les intègre dans un dictionnaire qui recense le nombre d'appartition
    de ces couleurs"""
    red = 0 
    for i in range(len(solution)-1,-1,-1): # Parcours de la boucle en sens inverse
        if solution[i] == attempt[i]:
            red += 1
            # On modifie la chaîne de caractères attempt pour enlever le couleur qui a déjà été décrite comme bien placée
            attempt = attempt[:i] + attempt[i+1:]
        elif solution[i] in dict.keys(): 
            # Si la couleur est déjà dans le dictionnaire, on augmente le nombre de cette couleur de 1
            dict[solution[i]] += 1
        else:
            # Si la couleur est pas encore dans le dictionnaire, on dit qu'elle y est une fois
            dict[solution[i]] = 1
    
    """Ensuite on regarde le nomre de blancs, en étudiant les couleurs encore présentes
    dans la chaine attempt par rapport à notre dictionnaire qui associe à chaque couleurs le nombre d'apparition"""
    white = 0 
    for element in attempt:
        if element in dict.keys() and dict[element] != 0: # Si la couleur est dans le dictionnaire (plus que 0 fois)
            white += 1
            dict[element] -= 1 # On dit que la couleur y est une fois de moins dans le disctionnaire
    return(red,white)


def test_evaluation():
    assert(evaluation("RVBJ","RMOB")) == (1,1)
    assert(evaluation("RRRR","RRRR")) == (4,0)
    assert(evaluation("RVBJ","MNOG")) == (0,0)
    assert(evaluation("RVBJ","JRVB")) == (0,4)
    assert(evaluation("RVVR","RVRV")) == (2,2)
    assert(evaluation("RRVV","VVRR")) == (0,4)
    assert(evaluation("RVRV","VRVR")) == (0,4)
    assert(evaluation("RVRN","NNOO")) == (0,1)

test_evaluation()