#!/usr/bin/env python3

import common

def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))
    
    global possibles
    possibles = []
    # Pour une version encore plus triviale, on pourrait aussi utiliser solution = ''.join([common.COLORS[0] for i in range(common.LENGTH)])


def codemaker(attempt):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument) en utilisant la fonction evaluation du fichier common
    """
    global solution
    global possibles
    if possibles == []:
        eval = common.evaluation(attempt, solution)
        possibles = common.donner_possibles(attempt,eval)
        print(solution)
        return eval
    else:
        count = 0
        solution_modit = solution
        for solution_tmp in possibles:
            possibles_tmp = possibles.copy()
            eval_tmp = common.evaluation(attempt, solution_tmp)
            common.maj_possibles(possibles_tmp, attempt, eval_tmp)
            tmp = len(possibles_tmp)
            if tmp > count:
                count = tmp
                solution_modif = solution_tmp
        solution = solution_modif
        eval = common.evaluation(attempt, solution)
        common.maj_possibles(possibles, attempt, eval)
        print(solution)
        return eval
            