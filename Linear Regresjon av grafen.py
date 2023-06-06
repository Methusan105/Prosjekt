import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Henter inn data fra url og leser den
url = "https://raw.githubusercontent.com/Methusan105/Prosjekt/main/Data.csv"
df = pd.read_csv(url, index_col=0)
x = df["year"]
y = df["gjennomsnitt"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def f(x):
  return slope * x + intercept

mymodel = list(map(f, x))

plt.scatter(x, y)
plt.plot(x, mymodel, label="Lineær Regresjonslinje")
plt.xlabel("År")
plt.ylabel("Gjennomsnitt")
plt.legend()
plt.grid()
plt.show()
