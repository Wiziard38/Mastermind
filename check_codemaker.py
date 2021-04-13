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
        longueur=len(possibles)
        
        while eval != (common.LENGTH,0):
            attempt =log.readline().strip()
            (red,white) = log.readline().strip().split(',')
            eval = (int(red),int(white))
            possibles2 = common.donner_possibles(attempt, eval)
            #common.maj_possibles(possibles, attempt, eval)
            #longueur2=len(possibles)
            # print(longueur2) #à enelever
            for i in possibles2:
                print(i)
                if i in possibles:
                    print("AAAAAAA")
                
                
            possible=possibles2
            
        print("Tout va bien, le codemaker n'a pas triché (de manière visible)")
                
check_codemaker('log')



