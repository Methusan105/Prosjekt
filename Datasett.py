import pandas as pd
import matplotlib as plt
url="/co2_mm_gl.csv"

df= pd.read_csv(url,index_col=0)
df 

x = df["time"] # x er en liste med datoer
y = df["value"] # y er en liste med priser
plt.plot(x, y)
plt.xlabel("Dato")
plt.ylabel("Pris")
plt.show()