import matplotlib.pyplot as plt 
import numpy as np 
phis = [20, 100, 1000, 1500]
availabilities = [0.999999176976224, 0.999999166325682, 0.999999040553661, 0.999998965509832]
plt.plot(phis,availabilities, marker='o')
plt.xlabel("MTTR")
plt.ylabel("Availabilities")
plt.grid(True)
plt.show()
