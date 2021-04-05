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

    
def evaluation(attempt, solution):
    """Fonction qui évalue un essai en fonction de la solution de référence.
    Renvoie un tuple composé du nombre de plots de la bonne couleur bien placés, 
    et du nombre de plots de la bonne couleur mais mals placés.
    """
    
    if len(solution) != len(attempt): # On vérifie que les deux chaînes ont la même longueur
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
    
    dict = {}
    """On va d'abord compter le nombre de rouges, les couleurs sont soit rouges,
    soit on les intègre dans un dictionnaire qui recense le nombre d'appartition
    de ces couleurs"""
    red = 0  # Nombre de plots bien placés
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
    white = 0 # Nombre de plots mal placés
    for element in attempt:
        if element in dict.keys() and dict[element] != 0: # Si la couleur est dans le dictionnaire (plus que 0 fois)
            white += 1
            dict[element] -= 1 # On dit que la couleur y est une fois de moins dans le disctionnaire
    return(red,white)


def donner_possibles(attempt, eval):
    """ Fonction qui renvoie un set comprenant toutes les combinaisons possibles 
    après une evaluation """
    # On va d'abord créer un set qui comprend toutes les combinaisons possibles
    def creer_possibles():
        """ Fonction qui nous donne toutes les possibilités de chaîne de taille LENGTH 
        parmis les couleurs COLORS. """
        count = 0
        set1 = set(COLORS)
        while count < LENGTH-1:
            set2 = set1.copy()
            for e in set2:
                for e2 in COLORS:
                    set1.add(e+e2)
            count += 1
            set1 = set1 - set2
        return set1
    possibles_ini = creer_possibles()
    
    # Maintenant on sél´ectionne uniquement les éléments qui correspondent à l'évaluation
    # (pour cela on utilise la symétrie de l'évaluation entre l'essai et la solution)
    possibles = set()
    for e in possibles_ini:
        if evaluation(str(e), attempt) == eval:
            possibles.add(e)
    return possibles


def maj_possibles(possibles, attempt, eval):
    """ Fonction qui modifie l'ensemble des possibiltés accordément avec un nouvel
    essai (une chaine attempt et l'évaluation associée """
    tmp = donner_possibles(attempt,eval)
    for element in possibles.copy():
        if element not in tmp:
            possibles.remove(element) # On cherche à supprimer sirectement sur la variable 'possibles'
    # Sans supprimer directement, on aurait pu simplement utiliser "possibles & donner_possibles(attempt,eval)"


## Fonctions de test

def test_evaluation():
    assert evaluation("RVBJ","RMOB") == (1,1)
    assert evaluation("RRRR","RRRR") == (4,0)
    assert evaluation("RVBJ","MNOG") == (0,0)
    assert evaluation("RVBJ","JRVB") == (0,4)
    assert evaluation("RVVR","RVRV") == (2,2)
    assert evaluation("RRVV","VVRR") == (0,4)
    assert evaluation("RVRV","VRVR") == (0,4)
    assert evaluation("RVRN","NNOO") == (0,1)


def test_donner_possibles():
    assert len(donner_possibles("RRRR", (0,0))) == 7**4 # Plus que 7 couleurs possibles
    assert len(donner_possibles("RVBG", (0,0))) == 4**4 # Plus que 4 couleurs possibles
    assert donner_possibles("RRRV", (2,2)) == {'RRVR','RVRR','VRRR'}
    assert len(donner_possibles("RRRR", (2,0))) == 6*7**2 # (nombre d'emplacements pour les deux rouges) * (nombre des chaines de longueurs 2 avec 7 couleurs possibles)
    assert len(donner_possibles("RRRR", (1,0))) == 4*7**3 # Même raisonnement
    assert len(donner_possibles("RROO", (1,1))) == len(donner_possibles("OORR", (1,1)))


def test_maj_possibles():
    possibles = {'RRRV','RRVR','RVRR','VRRR'}
    maj_possibles(possibles,'RRRV',(2,2)) 
    assert possibles == {'RRVR','RVRR','VRRR'}
    possibles = {'RRRV','RRRO','RRRG','RRRN','RRRM'}
    maj_possibles(possibles,'NGOV',(0,0)) 
    assert possibles == {'RRRM'}

if __name__ == '__main__':
    test_evaluation()
    test_donner_possibles()
    test_maj_possibles()
    