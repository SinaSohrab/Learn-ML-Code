import pandas as pd
import numpy as np
import matplotlib.pylab as plt

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)

data = np.concatenate((X, y), axis=1)
df = pd.DataFrame(data, columns=['X', 'y'])
df.to_csv("csv_create/test2.csv", index=False)

