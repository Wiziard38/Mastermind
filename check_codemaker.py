# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:44:09 2021

@author: ericg
"""
import os
import common

def check_codemaker(file):
    path = os.getcwd()
    log = open(path + "/logs/" + file + ".txt", "r") 
    
    
    #initialisation
    attempt =log.readline()
    (red,b,white,n)=tuple(log.readline())
    eval=(int(red),int(white))
    liste=common.donner_possibles(attempt.strip(),eval)
    print(liste)
    print(attempt)
    print(eval)
    
    #mise à jour des possibles
   # for i in range(1,len(file)-1):
    #    (red,white)=(int(lines[i+1][0]),int(lines[i+1][2]))
       # possibles=common.maj_possibles(possibles, lines[i], (red,white))
    #on vérifie si tous nos attempts apparaissent dans possibles
    #for l in range(0,int(len(file)/2)):
     #   if lines[2*l+1] not in possibles:
      #      return False

check_codemaker('log')
path = os.getcwd()
log = open(path + "/logs/" + 'log' + ".txt", "r") 





attempt =log.readline()
print(attempt)



#print(attempt)

