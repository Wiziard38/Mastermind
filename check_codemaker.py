# -*- coding: utf-8 -*-

import os
import common


def check_codemaker(file):
    path = os.getcwd()
    with open(path + "/logs/" + file + ".txt", "r") as log:
        # Initialisation :
        attempt =log.readline().strip()
        (red,white) = log.readline().strip().split(',')
        eval = (int(red),int(white))
        possibles = common.donner_possibles(attempt, eval)
        
        while eval != (4,0):
            attempt =log.readline().strip()
            (red,white) = log.readline().strip().split(',')
            eval = (int(red),int(white))
            if attempt not in possibles:
                print("Le codemaker à triché de manière visible !")
                return
            else:
                common.maj_possibles(possibles, attempt, eval)
        
        print("Tout va bien, le codemaker n'a pas triché (de manière visible)")


#check_codemaker('log')

def check_codemakerv2(file):
    path = os.getcwd()
    with open(path + "/logs/" + file + ".txt", "r") as log:
        # Initialisation :
        attempt =log.readline().strip()
        (red,white) = log.readline().strip().split(',')
        eval = (int(red),int(white))
        possibles = common.donner_possibles(attempt, eval)
        
        while eval != (4,0):
            attempt =log.readline().strip()
            (red,white) = log.readline().strip().split(',')
            eval1 = (int(red),int(white))
            if attempt not in possibles:
                (r1,b1)=eval1
                (r,b)=eval
                if r1>=r:
                    print("Le codemaker à triché de manière visible !")
                    return

            else:
                common.maj_possibles(possibles, attempt, eval1)
            eval=eval1
        print("Tout va bien, le codemaker n'a pas triché (de manière visible)")
                
check_codemakerv2('log')

