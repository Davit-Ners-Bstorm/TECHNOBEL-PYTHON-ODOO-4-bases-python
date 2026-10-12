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


nv_nb = int(input('Donne un autre nb : '))

# nv_var = 'PAIR' if nv_nb % 2 == 0 else 'IMPAIR'

# Un peu moche => block if elif classique svp
nv_autre = '1' if nv_nb == 1 else '2' if nv_nb == 2 else 'autre'

if nv_nb % 2 == 0:
    nv_var = 'PAIR'
else:
    nv_var = 'IMPAIR'

print(nv_var)
