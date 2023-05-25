import pandas as pd             # For å lese og behandle CSV-filer
import matplotlib.pyplot as plt # For plotting

url = "https://vincentarelbundock.github.io/Rdatasets/csv/quantreg/gasprice.csv"
# Vi leser inn data fra URLen og lagrer det i en dataframe som vi kaller df:
df = pd.read_csv(url, index_col=0)
df
# Metode 1

x = df["time"] # x er en liste med datoer
y = df["value"] # y er en liste med priser

plt.plot(x, y)
plt.xlabel("Dato")
plt.ylabel("Pris")
plt.show()