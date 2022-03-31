print('hello')

for i in range(2):
    print(f"Hello world! {i}")

# acesta este un comment pe o linie

"""
block
comment
"""


def new_function(a, b):
    return a + b


print(type(2))


l = []
n = []
n = "salut"
if not l:
    print('lista vida')

print(l is n)
print(l == n)

print(ord('a'))
print(chr(97))

print("""
bdhjad ncdd
dnejnd       ->        hbvub
    cnbejkbcej         cbek
""")


nume = 'Popescu'
prenume = 'Ion'

text = f"""
Buna ziua!

Ma numesc {nume} {prenume} 

Bine ati venit pe website-ul nostru!
"""
print(text)

l = [1, 2, 3]
print(l)
l[1] = 0
print(l)

name = 'Marius'
# da eroare
# name[0] = 'D'
print(name)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
g = l[:]
l[0] = 'a'
print(l)
print(g)


d = {'Nume': 'Zaharia', 'Prenume': "Marius", 'Varstas': '20'}

#print(d['Varsta'])
print(d.get('Varsta', 'Nu exista varsta'))

for key, value in d.items():
    print(f"{key} -> {value}")

s = {1, 2, 3}
c = {1, 2}

print(c.issubset(s))
print(c.intersection(s))
