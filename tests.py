#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports des fichiers utilisés :
import tmp_2
import common

def test_evaluation():
    """ Desc """
    assert tmp_2.evaluation("RVBJ","RMOB") == (1,1)
    assert tmp_2.evaluation("RRRR","RRRR") == (4,0)
    assert tmp_2.evaluation("RVBJ","MNOG") == (0,0)
    assert tmp_2.evaluation("RVBJ","JRVB") == (0,4)
    assert tmp_2.evaluation("RVVR","RVRV") == (2,2)
    assert tmp_2.evaluation("RRVV","VVRR") == (0,4)
    assert tmp_2.evaluation("RVRV","VRVR") == (0,4)
    assert tmp_2.evaluation("RVRN","NNOO") == (0,1)
    assert tmp_2.evaluation("RVRN","NNOO") == tmp_2.evaluation("NNOO", "RVRN")

def test_creer_possibles():
    """ Desc """
    assert len(common.creer_possibles()) == 4096


def test_donner_possibles():
    """ Desc """
    assert len(common.donner_possibles("RRRR", (0,0))) == 7**4 # Plus que 7 couleurs possibles
    assert len(common.donner_possibles("RVBG", (0,0))) == 4**4 # Plus que 4 couleurs possibles
    assert common.donner_possibles("RRRV", (2,2)) == {'RRVR','RVRR','VRRR'}
    assert len(common.donner_possibles("RRRR", (2,0))) == 6*7**2 # (nombre d'emplacements pour les deux rouges) * (nombre des chaines de longueurs 2 avec 7 couleurs possibles)
    assert len(common.donner_possibles("RRRR", (1,0))) == 4*7**3 # Même raisonnement
    assert len(common.donner_possibles("RROO", (1,1))) == len(common.donner_possibles("OORR", (1,1)))


def test_maj_possibles():
    """ Desc """
    possibles = {'RRRV','RRVR','RVRR','VRRR'}
    common.maj_possibles(possibles,'RRRV',(2,2))
    assert possibles == {'RRVR','RVRR','VRRR'}
    possibles = {'RRRV','RRRO','RRRG','RRRN','RRRM'}
    common.maj_possibles(possibles,'NGOV',(0,0))
    assert possibles == {'RRRM'}

if __name__ == '__main__':
    test_evaluation()
    test_creer_possibles()
    test_donner_possibles()
    test_maj_possibles()