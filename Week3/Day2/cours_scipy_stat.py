
# Asymétrie et kurtosis
# Qu'est-ce que l'asymétrie ?

# L'asymétrie mesure l'asymétrie de la distribution de probabilité d'une variable aléatoire à valeur réelle. Une asymétrie positive indique une queue sur le côté droit de la distribution, et une asymétrie négative indique une queue sur le côté gauche.

# Qu'est-ce que le Kurtosis ?

# Le kurtosis mesure la « traînée » de la distribution. Un kurtosis élevé signifie qu'une plus grande partie de la variance est due à des écarts extrêmes peu fréquents, par opposition à des écarts fréquents de taille modeste.

# Exemple concret d'asymétrie et de kurtosis :

# Considérons un ensemble de données représentant les tailles des hommes adultes dans une certaine région. Nous supposons que la distribution des tailles est normalement distribuée.

# Code Python pour le calcul :

import numpy as np
from scipy.stats import skew, kurtosis

# Example dataset (heights in cm)
heights = np.array([1, 2, 3])  # Example data

# Calculating skewness and kurtosis
skewness = skew(heights)
kurtosis_value = kurtosis(heights)

print("Skewness:", skewness)
print("Kurtosis:", kurtosis_value)