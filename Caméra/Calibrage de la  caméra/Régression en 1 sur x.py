import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Définir la fonction f(x) que vous souhaitez utiliser pour la régression
def f(x, a):
    return a/x

# Générer des données synthétiques avec un peu de bruit
x = [366.05,331.8,300.1,247.4,210,188,153.4,127,100.4,88.1,74.6,62.63,59,55.32,51.24,44.3,38.8,34.2,30.5,28.2,25.12,23.4,21.7] # sur l'ordi
y = [15,18,20,25,30,35,40,50,60,70,80,90,100,110,120,140,160,180,200,220,240,260,280]# en réel

# Régression des données
params, covariance = curve_fit(f, x, y)

# Récupérer les paramètres ajustés
a = params
a = 6096.14102686
# Créer une courbe ajustée avec les paramètres ajustés
x_fit = np.linspace(x[0], x[-1], 100)
y_fit = f(x_fit, a)

# Afficher les données et la courbe ajustée
plt.scatter(x, y, label='Données réelles')

plt.plot(x_fit, y_fit, 'r', label='Régression ajustée')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Régression selon f(x) = a/x')
plt.show()


