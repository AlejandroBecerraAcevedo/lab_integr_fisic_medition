# grafic histogram
import matplotlib.pyplot as plt
import pandas as pd

path = './dados.csv'

data = pd.read_csv(path, header=None, index_col=False)
print(data)

# count dataframe rows number how many  times the number 4 appears in the dataframe and print each row
counts = data == 4
print(counts.sum(axis=1))

desviacion = (9 * (1/6) * (1 - (1/6))) ** 0.5
print("Esta es la media probabilística: ", 9/6)
print("Esta es la desviación estándar: ", desviacion)


desviacion_total = ((20 * 0.05) * (1 - 0.05)) ** 0.5
print("Esta es la media probabilística total: ", 20 * 0.05)
print("Esta es la desviación estándar total: ", desviacion_total)


fig, ax = plt.subplots()

ax.hist(counts.sum(axis=1), bins=range(1, 11), align='left', rwidth=0.8)
plt.show()

prob = counts.sum(axis=1) / data.shape[1]