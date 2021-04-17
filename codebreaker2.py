import common
import numpy
import random

def init():
    """ Desc """
    global possibles
    possibles = set()
    
    global attempt
    attempt = ''

def codebreaker(evaluation_p):
    """ Desc """
    global possibles
    global attempt
    if evaluation_p == None:
        attempt = ''.join(common.choices(common.COLORS, common.LENGTH))
        return attempt
    elif possibles == set():
        possibles = common.donner_possibles(attempt,evaluation_p)
        attempt = random.sample(possibles,1)[0]
        return attempt
    else:
        common.maj_possibles(possibles, attempt, evaluation_p)
        attempt = random.sample(possibles,1)[0]
        return attempt