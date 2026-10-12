
# OPÉRATEURS ARITHMÉTIQUES

# Addition
# print(5 + 3)  # 8

# Division classique (retourne toujours un float)
# print(10 / 2)        # 5.0
# print(type(10 / 2))  # <class 'float'>
# print(5 / 2)         # 2.5

# Division entière (arrondit vers le bas)
# Avec deux entiers, le résultat est un int
# print(5 // 2)      # 2
# print(5.0 // 2)    # 2.0 (float)
# print(-5 // 2)     # -3

# Puissance
# print(2 ** 5)  # 32

# Modulo (reste de la division)
# print(10 % 3)  # 1

a = 1

# Ces deux écritures permettent d'effectuer
# la même opération : augmenter a de 1
a = a + 1
a += 1

# print(a)


# ==========================================
# OPÉRATEURS DE COMPARAISON
# ==========================================

# Égalité (compare les valeurs)
# print(a == 3)

# Différence
# print(a != 5)

# Supérieur / inférieur
# print(a > 3)
# print(a < 10)

# Supérieur ou égal / inférieur ou égal
# print(a >= 5)
# print(a <= 10)

# Les comparaisons retournent un booléen :
# True ou False

ma_list = [1, 2, 4, 3]

# Vérifie si une valeur est présente
# dans une collection
# print(2 in ma_list)      # True
# print(5 in ma_list)      # False

# ÉGALITÉ (==) VS IDENTITÉ (is)

# == compare les valeurs (le contenu)
# is vérifie si deux variables font référence
# exactement au même objet en mémoire

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

# list_a et list_b référencent le même objet
print(list_a is list_b)  # True

# list_a et list_c ont le même contenu,
# mais ce sont deux objets différents
print(list_a == list_c)  # True
print(list_a is list_c)  # False

a = [1, 2, 3]
b = a

# Les deux variables référencent la même liste
# Modifier cette liste affectera donc les deux variables
a.append(18)

# print(a)  # [1, 2, 3, 18]
# print(b)  # [1, 2, 3, 18]

# Attention : modifier un objet et réaffecter
# une variable sont deux choses différentes !

a = [5, 6, 7]

# Ici, a référence une nouvelle liste
# mais b référence toujours l'ancienne
# print(a)  # [5, 6, 7]
# print(b)  # [1, 2, 3, 18]

a = 5
b = 5

# En CPython, certains petits entiers sont
# réutilisés en mémoire pour optimiser les performances
# print(a is b)  # True (dans CPython)

b = 7

# b référence maintenant un autre objet
# print(a is b)  # False

# IMPORTANT :
# On utilise == pour comparer des valeurs !
# On évite d'utiliser is pour comparer des nombres.

# OPÉRATEURS LOGIQUES

c = True
d = False

# AND : True si les deux conditions sont vraies
print(c and d)  # False

# OR : True si au moins une condition est vraie
print(c or d)   # True

# NOT : inverse la valeur booléenne
print(not c)    # False

# On peut combiner plusieurs comparaisons
age = 20

# print(age >= 18 and age < 65)  # True

# Python permet aussi les comparaisons chaînées
# print(18 <= age < 65)  # True
