import common
import numpy
import random

def init():
   global possibles
   possibles = []
   global attempt
   attempt = ''

def codebreaker(evaluation_p):
    """ Desc """
    global possibles
    global attempt
    if evaluation_p == None:
        attempt = ''.join(common.choices(common.COLORS, common.LENGTH))
        return attempt
    elif possibles == []:
        possibles = common.donner_possibles(attempt,evaluation_p)
        print(possibles)
        attempt = random.sample(possibles,1)[0]
        return attempt
    else:
        common.maj_possibles(possibles, attempt, evaluation_p)
        print(possibles)
        attempt = random.sample(possibles,1)[0]
        return attempt