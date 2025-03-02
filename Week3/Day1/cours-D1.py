import numpy as np
print(np.__version__)

import random 

# # Example 1
# # Example 2D array
# array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Accessing a single element
# print("Element at row 1, column 2:", array_2d[1, 2])  # Output: 6

# # Accessing a row
# print("Second row:", array_2d[1, :])  # Output: [4 5 6]

# # Accessing a column
# print("Third column:", array_2d[:, 2])  # Output: [3 6 9]


# # Exercice: 
# #1. Indexation de base : créez un tableau de 10 éléments et accédez au 5ème élément.
# array = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# # 2. Découpage de base : à partir du même tableau, extrayez une tranche contenant les 3e à 8e éléments.

# array_1= array[2 : 8]

# print(array_1)
# # 3. Indexation booléenne : Créez un tableau de 6 entiers aléatoires compris entre 10 et 50. Imprimez les éléments supérieurs à 30.

# table = np.random.randint(10, 51, size =6)
# print(table)


# 4. Indexation fantaisie : à partir du même tableau, utilisez l'indexation fantaisie pour accéder aux 2e, 4e et 6e éléments.

# Résultat attendu :

# Le 5ème élément du premier tableau.
# Une tranche du tableau montrant les éléments de la 3ème à la 8ème position.
# Éléments supérieurs à 30 du tableau aléatoire.
# Éléments sélectionnés (2e, 4e, 6e) à partir du tableau aléatoire à l'aide d'une indexation sophistiquée.

# # #Exerciceé: 
# # A one dimensional array with the temperatures from this week.
# # A two dimensional array of shape 2,5 with random values (choose them yourself) from 1 to 10.
# # A 3D array with valid pixel values for a picture with 9 pixels.
# temperature_array = np.random.normal( loc = 4, scale =2, size= 7)
# print(temperature_array)

# array_2d = np.arange(10).reshape(2, 5)
# print(array_2d)











# #Excercice: Reshape
# #1. Reshape Array: Create a 1D array with 12 elements and reshape it to a 4x3 matrix. Then reshape it to a 2x6 matrix.
# array_1D = np.random.rand(12)
# print(array_1D)

# array_1D_reshaped = array_1D.reshape(3, 4)
# print(array_1D_reshaped)


# new_matrix = array_1D_reshaped.reshape(2, 6)
# print(new_matrix)

# new_matrix_tansposed = new_matrix.T
# print(new_matrix_tansposed)

# # array = np.random.rand(365)

# # array_2 = array[:364].reshape(52, 7)

# # print(array_2)
x = np.array([1, 2, 3, 4, 5, 6, 7])
new = np.random.permutation(x)
print(new)