from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import *
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

# Henter inn data fra url og leser den
url = "https://raw.githubusercontent.com/Methusan105/Prosjekt/main/Data.csv"
df = pd.read_csv(url, index_col=0)
x = df["year"]
y = df["gjennomsnitt"]

# Utfører lineær regresjon
poly = PolynomialFeatures(degree=2)
X = poly.fit_transform(np.array(x).reshape(-1, 1))
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plotter data og regresjonslinje
plt.scatter(x, y, label="Observasjoner")
plt.plot(x, y_pred, color='red', label="Regresjonslinje")
plt.xlabel("År")
plt.ylabel("Gjennomsnitt")
plt.legend()
plt.show()