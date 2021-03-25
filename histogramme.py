


# Ancien code pour tracer un histo
days = []
number = []


plt.hist(np.array(days), bins=np.array(range(1,368)), weights=np.array(number))
plt.title("fréquence des jours d'anniversaires") 
plt.show()