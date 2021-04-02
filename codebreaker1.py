import common
import numpy

def init():
    global liste
    liste = []

def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie). Cette version triviale n'utilise pas cette information, puisqu'
    elle joue au hasard.
    """
    global liste
    while True:
        tmp = ''.join(common.choices(common.COLORS, common.LENGTH))
        if tmp not in liste:
            liste.append(tmp)
            return tmp