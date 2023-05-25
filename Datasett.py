import pandas as pd
import matplotlib.pyplot as plt
url="https://raw.githubusercontent.com/Methusan105/Prosjekt/main/co2_annmean_gl.csv"

df= pd.read_csv(url,index_col=0)
df 

x = df["Year"] # x er en liste med datoer
y = df["Gjennomsnitt"] # y er en liste med priser
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Pris")
plt.show()