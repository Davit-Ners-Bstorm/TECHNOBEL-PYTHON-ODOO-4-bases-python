# Declaration de variable sans declaration de type explicite, direct variable = valeur
prenom = 'Jean'
age = 30

# print(type(prenom))

# Convention : snake_case
first_name = "Jean"

# Typage dynamique, reassigner valeur d'un autre type à une variable
# prenom = 42

# print(type(prenom))

# message = "Je m'appelle " + prenom

# "f-string" => permet d'injecter des variables dans une chaine de charactère
message = f"Je m'appelle {prenom}"

# print(message)

# Affectation multiple
x = y = z = 0

# Affectation parallèle
a = 5
b = 7
c = 13

a, b, c = c, a, b

# print(f"a = {a}, b = {b}, c = {c}")


# Type de données

# list (array/tableau)
ma_list = [1, 2, 3]

# tuples
mon_tuple = (1, 2, 3)

# set
mon_set =  {5, 1, 2, 3, 1}

# print(mon_set)

# dict
mon_dico = {
    "lieu": 'LLN',
    "name": 'Prefo ODOO',
    "nb_stagiaires": 16,
    "list_formateurs": [
        {
            "nom": "Davit"
        },
        {
            "nom": "Sebastien"
        }
    ]
}


# Conversions

# conversion en int
douze = '12'
# print(type(douze))

douze_en_int = int(douze)
# print(type(douze_en_int))

# Conversion en string
qqch = 42
qqch_en_str = str(qqch)
# print(type(qqch_en_str))

# Eval => execute code passé en string en paramètre =>>> Attention, dangeureux si on y execute une entrée utilisateur sans contrôle
resultat = eval("1 + 1")
print(resultat)

# Exo 1
