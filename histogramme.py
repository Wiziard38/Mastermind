import common
import random
import matplotlib.pyplot as plt
import numpy as np


def trace_histo(n):
    list = []
    p = len(common.COLORS)**common.LENGTH
    for i in range(n):
        proba = True
        nbr_essais = 0
        while proba:
            if random.randint(0,p) == 0:
                list.append(nbr_essais)
                proba = False
            nbr_essais +=1
    plt.hist(list, range = (0,8000), bins = 8000, color='red')
    plt.title("Nombres d'essais") 
    plt.show()
    

def trace_histo2(n): # methode 2
    p = len(common.COLORS)**common.LENGTH
    list2 = np.random.geometric(1/p, n)
    plt.hist(list2, range = (0,8000), bins = 8000, color='yellow')
    plt.title("Nombres d'essais") 
    plt.show()
