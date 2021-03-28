import common

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
    liste.append(evaluation_p)
    while True:
        tmp = ''.join(common.choices(common.COLORS, common.LENGTH))
        if tmp not in liste:
            return tmp

global liste