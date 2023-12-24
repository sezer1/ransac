import numpy as np
import matplotlib.pyplot as plt

def generateDatasetNPL(n, m, c, var=1., limits=(0,10)):
    """ n: nokta sayisi, m: dogru egimi, c: y'yi kestigi yer """
    x = np.arange(limits[0], limits[1], 0.01)
    v = np.random.normal(scale=var,size=len(x))
    y = m*x + c + v
    indices = np.random.choice(len(y),size=n)
    ds = np.vstack((x[indices],y[indices]))
    return ds.T

ds = generateDatasetNPL(10, 2, 3)
plt.scatter(ds[:,0],ds[:,1])
plt.show()