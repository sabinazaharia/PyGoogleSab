"""
Să se scrie un modul care contine 3 funcții recursive care primesc ca parametru un număr întreg și returnează:
○ suma tuturor numerelor de la [0, n]
○ suma numerelor pare de la [0, n]
○ suma numerelor impare de la [0. n]
"""

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)


print(recur_sum(3))

def sum_even(n):
    sum = 0
    for e in range(n+1):
        if(e % 2 == 0):
            sum = sum + e

    return sum

print(sum_even(10))

def sum_odd(n):
    sum = 0
    for e in range(n+1):
        if(e % 2 != 0):
            sum = sum + e

    return sum

print(sum_odd(10))