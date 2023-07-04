import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#--bilioane-de-dolari-pe-an-samsung--

revenue2 = (203.44 + 240.72 + 241.6) / 3
revenue3 = (240.72 + 241.6 + revenue2) / 3
revenue4 = (241.6 + revenue2 + revenue3) / 3
revenue = np.array(list([106.74, 104.33, 113.64, 133.95, 146.44, 184.22, 210.86, 195.23, 174.66, 175.5, 214.57, 221.67, 198, 203.44, 240.72, 241.6]))
lista_an = np.array(list(range(1, len(revenue) + 1)))
an = lista_an + 2006
data = { "revenue": revenue}
df = pd.DataFrame(data, index=an)

df["MA3"] = df["revenue"].rolling(3).mean().shift(1)

df.plot()

df["er3"] = np.power((df["revenue"] - df["MA3"]),2)
df["MA4"] = df["revenue"].rolling(4).mean().shift(1)
df["er4"] = np.power((df["revenue"] - df["MA4"]),2)
df["MA5"] = df["revenue"].rolling(5).mean().shift(1)
df["er5"] = np.power((df["revenue"] - df["MA5"]),2)
df["MA6"] = df["revenue"].rolling(6).mean().shift(1)
df["er6"] = np.power((df["revenue"] - df["MA6"]),2)

MSE3 = df["er3"].mean()
MSE4 = df["er4"].mean()
MSE5 = df["er5"].mean()
MSE6 = df["er6"].mean()

print(df)
print(f"MSE3 : {MSE3}\nMSE4 : {MSE4}\nMSE5 : {MSE5}\nMSE6 : {MSE6}\n")
print(f"revenue2 : {revenue2}\nrevenue3 : {revenue3}\nrevenue4 : {revenue4}\n")

plt.show()
