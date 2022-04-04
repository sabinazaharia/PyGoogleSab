from my_package.my_module import my_var as module_var, my_func as module_func
from my_package.my_second_module import *

my_var = 6
if __name__ == '__main__':
    print('Hello world')
    print(module_var)
    print(my_var)
    print(module_func())