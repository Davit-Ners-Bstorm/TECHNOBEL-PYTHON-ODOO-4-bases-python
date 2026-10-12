# input => Permet de prendre une entrée utilisateur dans la console, programme mis en pause en attendant 

# prenom = input("Donne ton nom : ") -> entrée utilisateur stockée dans la variable 'prenom'

# print(f"Tu t'appelles {prenom}")

# Paramètre 'sep' => permet de definir un separateur qui sera placé entre les differents elements prints (' ' par defaut)

# Paramètre 'end' permet de definir charactère placé à la fin du print (\n par defaut)
# print('hello', 'bonjour', 'hallo', sep='-', end=".\n")
# print(1)
# print(2)

# Exercices
# 1
# nom = input('Donne ton nom : ')
# prenom = input('Donne ton prenom : ')

# print(nom, prenom, sep='_')

# 2
print('message1', 'fin du message', end='!\n')
print('message2', 'fin du message', end='!\n')

# 3
print('hello', 'world', sep='')

# 4
nb1 = int(input('Donne nb1 : '))
nb2 = int(input('Donne nb2 : '))

print(f"{nb1} + {nb2} = {nb1 + nb2}")
