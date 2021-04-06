#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Test des fonctions de common.py
import common

def test_evaluation():
    assert common.evaluation("RVBJ","RMOB") == (1,1)
    assert common.evaluation("RRRR","RRRR") == (4,0)
    assert common.evaluation("RVBJ","MNOG") == (0,0)
    assert common.evaluation("RVBJ","JRVB") == (0,4)
    assert common.evaluation("RVVR","RVRV") == (2,2)
    assert common.evaluation("RRVV","VVRR") == (0,4)
    assert common.evaluation("RVRV","VRVR") == (0,4)
    assert common.evaluation("RVRN","NNOO") == (0,1)


def test_donner_possibles():
    assert len(common.donner_possibles("RRRR", (0,0))) == 7**4 # Plus que 7 couleurs possibles
    assert len(common.donner_possibles("RVBG", (0,0))) == 4**4 # Plus que 4 couleurs possibles
    assert common.donner_possibles("RRRV", (2,2)) == {'RRVR','RVRR','VRRR'}
    assert len(common.donner_possibles("RRRR", (2,0))) == 6*7**2 # (nombre d'emplacements pour les deux rouges) * (nombre des chaines de longueurs 2 avec 7 couleurs possibles)
    assert len(common.donner_possibles("RRRR", (1,0))) == 4*7**3 # Même raisonnement
    assert len(common.donner_possibles("RROO", (1,1))) == len(common.donner_possibles("OORR", (1,1)))


def test_maj_possibles():
    possibles = {'RRRV','RRVR','RVRR','VRRR'}
    common.maj_possibles(possibles,'RRRV',(2,2)) 
    assert possibles == {'RRVR','RVRR','VRRR'}
    possibles = {'RRRV','RRRO','RRRG','RRRN','RRRM'}
    common.maj_possibles(possibles,'NGOV',(0,0)) 
    assert possibles == {'RRRM'}

if __name__ == '__main__':
    test_evaluation()
    test_donner_possibles()
    test_maj_possibles()
    