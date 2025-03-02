import numpy as np
import scipy.stats as stats

# Exemple de données : tailles en centimètres
# Pour cet exemple, nous générons des données aléatoires autour d'une moyenne (par exemple 175 cm)
np.random.seed(0)
heights = np.random.normal(loc=175, scale=10, size=100)

# Calcul de l'asymétrie (skewness)
skewness = stats.skew(heights)
print("Skewness (asymétrie) :", skewness)

# Calcul du kurtosis (en excès, c'est-à-dire kurtosis - 3)
kurtosis_excess = stats.kurtosis(heights)
print("Excess Kurtosis :", kurtosis_excess)

