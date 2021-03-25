import common
from random import random.randint


def trace_histo(n):
    nbr_essais = []
    global LENGHT
    global couleur
    q = LENGHT *len(couleurs)
    for i in range(n):
        count = 0
        while count == 0:
            if randint(0,q) == 0:
                nbr_essais.append(count)
                
    

plt.hist(np.array(days), bins=np.array(range(1,10000)), weights=np.array(number))
plt.title("fréquence des jours d'anniversaires") 
plt.show()
