# Tema 1

"""
declararea unei liste care să conțină elementele
7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

"""

lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)

"""
afișarea unei alte liste ordonată ascendent 
(lista inițială trebuie păstrată în aceeași formă)
"""
lista_ordonata_asc = lista.copy()
lista_ordonata_asc.sort()
print(lista_ordonata_asc)


"""
afișarea unei liste ordonată descendent 
(lista inițială trebuie păstrată în aceeași formă)
"""
lista_ordonata_desc = list(lista)
lista_ordonata_desc.sort(reverse=True)
print(lista_ordonata_desc)

"""
afișarea numerelor de pe pozitii pare din listă 
(folosind DOAR slice, altă metodă va fi considerată invalidă)
"""
lista_numere_pare = lista_ordonata_asc[0::2]
print(lista_numere_pare)

"""
afișarea numerelor de pe pozitii impare din listă 
(folosind DOAR slice, altă metodă va fi considerată invalidă)
"""
lista_numere_impare = lista_ordonata_asc[1::2]
print(lista_numere_impare)

"""
afișarea elementelor multipli ai lui 3
"""
for e in lista:
    if e%3 == 0:
        print(e)