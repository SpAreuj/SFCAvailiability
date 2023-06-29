import numpy as np
import seaborn as sns
import scipy.io
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
data = scipy.io.loadmat('repairs_gr2.mat')
x = data['repairs']
print("Quantità dati per le repair: "+str(len(x)))
print("media aritmentica dei valori di repair: " +str(np.mean(x)))
sns.set_style('whitegrid')
"""sns.kdeplot(x, ax=ax)
plt.title("Repairs Distribution")
plt.xlabel("Time")
plt.ylabel("Density")
ax.set_xlim(0)
plt.legend('',frameon=False)
plt.show()"""


censored = scipy.io.loadmat('censoring_gr2.mat')
y = censored["censoring"]
print("Quantità dati censurati per i fails: "+ str(np.sum(y)))

failed = scipy.io.loadmat("failures_gr2.mat")
z=failed["failures"]
print("Numero totale fails:"+str(len(z)))
"""sns.kdeplot(z, ax=ax)
plt.title("Failures with censored data Distribution")
plt.xlabel("")
plt.ylabel("")
ax.set_xlim(0)
plt.legend('',frameon=False)
plt.show()"""


not_censored_fails=z[y==0]
censored_fails=z[y==1]
"""sns.kdeplot(not_censored_fails, ax=ax)
plt.title("Failures without censored data Distribution")
plt.xlabel("")
plt.ylabel("")
ax.set_xlim(0)
plt.legend('',frameon=False)
plt.show()"""



"""print("Media fails non censurati:"+str(np.mean(not_censored_fails)))
print("Somma fails non censurati: "+str(np.sum(not_censored_fails)))
print("Valore fails censurati: "+ str(censored_fails))
print("Massimo dei tempi di fail:"+ str(np.max(z)))"""
print("CENSURA DI TIPO 1 per failure")
print("Stima MTTF: " + str(np.sum(z)/len(not_censored_fails)))
print("NESSUNA CENSURA per repair")
print("Stima MTTR: " + str(np.sum(x)/len(x)))


