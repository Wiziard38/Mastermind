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
    (red,white) = (0,0)
    dict = {}
    for i in range(len(solution)):
        if solution[i] == attempt[i]:
            red += 1
        elif attempt[i] in dict.values():
            white += 1
            del dict[i]
        else:
            dict[i] = solution[i]
    return (red,white)
                                        
                    
def test_evaluation():
    assert(evaluation("RVBJ","RMOB")) == (1,1)
    assert(evaluation("RVBJ","RMOR")) == (1,0)
    assert(evaluation("RVBJ","RVJB")) == (2,2)
    assert(evaluation("RVBJ","RMOB")) == (1,1)
    
test_evaluation()