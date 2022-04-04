# # Cursul 3
#
# import random
# choices = [x for x in range(11)]
# print(choices)
# while True:
#     random_choice = random.choice(choices)
#     if random_choice % 3 == 0:
#         break
#     print(f'random_choice {random_choice}')
#
# print(f'last random_choice {random_choice}')
#
#
# def my_sum(a, b):
#     return a+b
#
#
# print(my_sum(1, 2))
#
# """
# Parametrii se trimit in functie prin referinta, nu prin valoare
# Daca vrem sa nu modificam lista initiala, trebuie sa facem o copie in interiorul func
# """
# my_list = [1, 2, 3]
#
#
# def my_function(list_param):
#     list_param = list_param.copy()
#     """
#     SAU
#     list_param = list_param[::]
#     list_param = list(list_param)
#     """
#     list_param.append(4)
#
#
# my_function(my_list)
# print(my_list)
#
# # Args preia toate argumentele nespecificate
# def sum(*args):
#     acc = 0
#     for arg in args:
#         acc += arg
#     return acc
#
#
# print(f'Suma totala {sum(1,2,3,4,5,6)}')
#
#
# # Tratarea exceptiilor
#
# my_var = input('Introduceti un numar:')
# try:
#     my_int = int(my_var)
#     print(my_int)
# except ValueError as e:
#     print('Introduceti un numar valid')
# except NameError as e:
#     print('Pentru dev, ai grija la cod')
# else:
#     print('Ajugem aici daca nu avem exceptii')
# finally:
#     print('Ajungem aici oricum, cu sau fara exceptii')


#print(dir(__builtins__))

# Namespace enclosing

def my_function():
    def my_second_function():
        print(f'My second function {msg}')

    msg = 'Hello'

    my_second_function()
    print(f'My function {msg}')


my_function()






