#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports des fichiers utilisés :
import common

def test_evaluation():
    """ Fonction test de la fonction evaluation du fichier common.py.
    Le but ici est de vérifier avec diverses combinaisons, dont on connait l'évaluation que la focntion ne pose pas de problèmes. """
    if len(common.COLORS) == 8 and common.LENGTH == 4:
        assert common.evaluation("RVBJ","RMOB") == (1,1)
        assert common.evaluation("RRRR","RRRR") == (4,0)
        assert common.evaluation("RVBJ","MNOG") == (0,0)
        assert common.evaluation("RVBJ","JRVB") == (0,4)
        assert common.evaluation("RVVR","RVRV") == (2,2)
        assert common.evaluation("RRVV","VVRR") == (0,4)
        assert common.evaluation("RVRV","VRVR") == (0,4)
        assert common.evaluation("RVRN","NNOO") == (0,1)
        assert common.evaluation("RVRN","NNOO") == common.evaluation("NNOO", "RVRN")

def test_creer_possibles():
    """ Fonction test de la fonction creer_possibles du fichier common.py, pour un cas précis dont on connait le résultat. """
    assert len(common.creer_possibles()) == len(common.COLORS)**common.LENGTH


def test_donner_possibles():
    """ Fonction test de la fonction donner_possibles du fichier common.py, pour quelques cas précis dont on connait le résultat. """
    if len(common.COLORS) == 8 and common.LENGTH == 4:
        assert len(common.donner_possibles("RRRR", (0,0))) == 7**4 # Plus que 7 couleurs possibles
        assert len(common.donner_possibles("RVBG", (0,0))) == 4**4 # Plus que 4 couleurs possibles
        assert common.donner_possibles("RRRV", (2,2)) == {'RRVR','RVRR','VRRR'}
        assert len(common.donner_possibles("RRRR", (2,0))) == 6*7**2 # (nombre d'emplacements pour les deux rouges) * (nombre des chaines de longueurs 2 avec 7 couleurs possibles)
        assert len(common.donner_possibles("RRRR", (1,0))) == 4*7**3 # Même raisonnement
        assert len(common.donner_possibles("RROO", (1,1))) == len(common.donner_possibles("OORR", (1,1)))


def test_maj_possibles():
    """ Fonction test de la fonction maj_possibles du fichier common.py, pour deux cas simplistes dont on connait le résultat. """
    if len(common.COLORS) == 8 and common.LENGTH == 4:
        possibles = {'RRRV','RRVR','RVRR','VRRR'}
        common.maj_possibles(possibles,'RRRV',(2,2))
        assert possibles == {'RRVR','RVRR','VRRR'}
        possibles = {'RRRV','RRRO','RRRG','RRRN','RRRM'}
        common.maj_possibles(possibles,'NGOV',(0,0))
        assert possibles == {'RRRM'}

if __name__ == '__main__':
    # On exécute nos différentes fonctions de tests, si rien ne s'affiche c'est qu'aucune erreur n'a été relevée !
    test_evaluation()
    test_creer_possibles()
    test_donner_possibles()
    test_maj_possibles()