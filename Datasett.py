import pandas as pd
import matplotlib.pyplot as plt
url="https://raw.githubusercontent.com/Methusan105/Prosjekt/main/Data.csv"

df= pd.read_csv(url,index_col=0)
df 

x = df["year"] # x er en liste med datoer
y = df["gjennomsnitt"] # y er en liste med priser
plt.plot(x, y)
plt.xlabel("År")
plt.ylabel("Gjennomsnitt")
plt.show()