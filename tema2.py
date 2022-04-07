"""
Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor
care reprezintă numere întregi sau reale.
○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
○ your_function() va returna 0.
○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

"""

def my_function(*args, **kwargs):
    sum = 0
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            sum = sum + arg
    return sum

print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))


"""
Să se scrie o funcție care citește de la tastatură și returnează valoarea 
dacă aceasta este un număr întreg, altfel returnează valoarea 0.

"""
my_var = input('Introduceti ceva:')


def numar_intreg(x):
    try:
        int(x)
    except ValueError:
        print('0')
    else:
        print(x)


numar_intreg(my_var)

"""
Să se scrie un modul care contine 3 funcții recursive care primesc ca parametru un număr întreg și returnează:
○ suma tuturor numerelor de la [0, n]
○ suma numerelor pare de la [0, n]
○ suma numerelor impare de la [0. n]

"""