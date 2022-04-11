# Curs 5 - OOP

# print(type(int))
# print(type(float))

class MyFirstClass:
    pass


my_first_python_object = MyFirstClass()


class Dog:
    legs_no = 4

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{type(self)} - {self.name}'

    def change_name(self, name):
        self.name = name

    #poate fi apelata din clasa si dintr-o instanta de clasa
    @staticmethod
    def speak():
        print('Bark! Bark!')


my_dog = Dog('Rex')
print(my_dog)

my_dog.speak()

Dog.speak()
# speak merge ptc e statica, dar change name da eroare
# Dog.change_name('ehe')

print(my_dog.legs_no)
print(Dog.legs_no)