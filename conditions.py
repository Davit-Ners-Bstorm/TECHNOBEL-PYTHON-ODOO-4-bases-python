import random


# # Structures conditionnelles

# nb = int(input('Donne un nb : '))

# if nb == 42:
#     print('BOOM NB magique')

# if nb > 10 and nb % 2 == 0:
#     print('plsu grand que 10 et pair')
# elif nb > 5:
#     print('Plus grand que 5')
# elif nb > 3:
#     pass
# else:
#     print('Pas plus grand que 10')

# match nb:
#     case 5 | 6:
#         print('CIIIINQ')
#         print('hey')
#     # case 6:
#     #     print('SIIIIX')
#     case 7:
#         pass
#     case _:
#         print('Autre')


# nv_nb = int(input('Donne un autre nb : '))

# nv_var = 'PAIR' if nv_nb % 2 == 0 else 'IMPAIR'

# Un peu moche => block if elif classique svp
# nv_autre = '1' if nv_nb == 1 else '2' if nv_nb == 2 else 'autre'

# if nv_nb % 2 == 0:
#     nv_var = 'PAIR'
# else:
#     nv_var = 'IMPAIR'

# print(nv_var)


# Exercices
# 1
# type_de_cafe = input("Choix du type de cafe : 'regular', cappuccino, 'americano'")
# taille_du_cafe = input("Taille ? small, medium, large")
# extra = input('extra ? lait ou sucre')

# match type_de_cafe:
#     case "regular":
#         prix_total = 2.5
#     case "cappuccino":
#         prix_total = 3
#     case "americano":
#         prix_total = 4.5
#     case _:
#         prix_total = 3
#         type_de_cafe = 'regular'

# if taille_du_cafe == 'small':
#     prix_total *= 0.8
# elif taille_du_cafe == 'medium':
#     pass
# elif taille_du_cafe == 'large':
#     prix_total *= 1.25

# sucre = False
# lait = False
# if 'sucre' in extra:
#     sucre = True
#     prix_total += 0.3
# if 'lait' in extra:
#     lait = True
#     prix_total += 0.5

# print(f"Ton cafe: {taille_du_cafe} {type_de_cafe} {"avec" if sucre else "sans"} sucre")
# print(f"{prix_total:.2f}")


# 2
# inpu = int(input("veuillez rentre une note entre 0 et 20"))

# match inpu :
#     case inpu if inpu > 20 or inpu < 0 :
#         print("wrong input")
#     case inpu if inpu > 17 :
#         print("A")
#     case inpu if inpu > 14 : 
#         print("B")
#     case inpu if inpu > 12 :
#         print("C")
#     case inpu if inpu > 10 :
#         print("D")
#     case _ : 
#         print("F")


# 3

# nombre_magique = random.randint(1,50)

# input_utilisteur = int(input("Veuillez entrer un nombre : "))

# if input_utilisteur == nombre_magique :
#     print("Bravo, vous êtes un champion")

# elif input_utilisteur>nombre_magique :
#     print("Plus grand")
# else :
#     print("Plus petit")

# print("Le nombre a trouver était : ", nombre_magique)


# 4
# weight = float(input("Please enter your weight : "))
# height = float(input("Please enter your height : "))

# bmi = weight / height ** 2
# bmi_indicator = ""

# if bmi < 18.5:
#     bmi_indicator = "Underweight"

# elif bmi < 25:
#     bmi_indicator = "Normal"

# elif bmi < 30:
#     bmi_indicator = "Overweight"

# else:
#     bmi_indicator = "Obese"

# print(bmi, bmi_indicator, sep=" - ")


# 5
# print("Bienvenue dans le terminal de citatitons")
# theme = int(input("choisissez un theme parmis :\n 1 : Motivation; 2 : Vie; 3 : Sagesse; 4 : Relations; 5 : Créativité. \n"))
 
# citations = [
#             ""
#             "Le succès vient à ceux qui persévèrent.",
#             "Les grandes choses prennent du temps.",
#             "La persévérance surpasse le talent.",
#             "Les défis forgent le caractère.",
#             "Les rêves exigent du travail.",
#             "La discipline mène à la liberté.",
#             "Les erreurs sont des marches vers le succès.",
#             "La réussite est un état d’esprit.",
#             "Les opportunités se créent.",
#             "La persévérance est la clé de l’impossible."
#             "La vie est un voyage, pas une destination.",
#             "Chaque jour est une nouvelle chance.",
#             "Le bonheur se trouve dans les petites choses.",
#             "Apprends d’hier, vis aujourd’hui, espère demain.",
#             "La vie est faite de choix, pas de hasard.",
#             "Le temps est le bien le plus précieux.",
#             "La vie est un cadeau à apprécier.",
#             "Les petites actions font de grandes différences.",
#             "La paix commence en soi.",
#             "La joie se partage."
#             "La connaissance est une richesse qui ne s’épuise pas.",
#             "Les échecs sont des leçons déguisées.",
#             "La vérité finit toujours par éclater.",
#             "La sagesse vient avec l’expérience.",
#             "La curiosité ouvre des horizons.",
#             "L’humilité précède la grandeur.",
#             "La simplicité est la sophistication ultime.",
#             "Les bonnes habitudes façonnent l’avenir.",
#             "La force vient de l’intérieur.",
#             "Les pensées positives attirent le positif."
#             "La gentillesse est un langage universel.",
#             "Le respect est le fondement de toute relation.",
#             "La confiance en soi ouvre toutes les portes.",
#             "Les mots peuvent changer le monde.",
#             "La beauté est dans le regard que l’on porte.",
#             "La confiance se gagne et se mérite.",
#             "La confiance est le ciment des relations.",
#             "L’amour est la plus grande force.",
#             "La joie est contagieuse.",
#             "Les rêves nourrissent l’âme."
#             "Les rêves donnent un sens à la vie.",
#             "La créativité est l’intelligence qui s’amuse.",
#             "La lumière brille plus fort dans l’obscurité.",
#             "La passion donne de l’énergie à l’action.",
#             "Les petites actions font de grandes différences.",
#             "Les opportunités se créent.",
#             "La curiosité ouvre des horizons.",
#             "Les mots peuvent changer le monde.",
#             "La beauté est dans le regard que l’on porte.",
#             "La joie se partage."
#     ]
 
# check = True
 
# match theme:
#     case 1:
#         choice = random.randint(1, 10)
#         citation = citations[choice]
#     case 2:
#         choice = random.randint(10, 20)
#         citation = citations[choice]
#     case 3:
#         choice = random.randint(20, 30)
#         citation = citations[choice]
#     case 4:
#         choice = random.randint(30, 40)
#         citation = citations[choice]
#     case 5:
#         choice = random.randint(40, 50)
#         citation = citations[choice]
#     case _:
#         print("votre choix est invalide")
#         check = False
 
# if check : print(citation)
