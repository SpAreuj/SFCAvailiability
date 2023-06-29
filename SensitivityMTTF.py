import matplotlib.pyplot as plt 
import numpy as np 
lambdas = [1500, 1250, 750, 500]
availabilities = [0.999999178296708, 0.999999155050243, 0.999999057656182, 0.999998925702479]
plt.plot(lambdas,availabilities, marker='o')
plt.xlabel("MTTF")
plt.ylabel("Availabilities")
plt.grid(True)
plt.show()
