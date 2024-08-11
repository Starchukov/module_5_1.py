#Создайте класс House.
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range (new_floor):
            j = i + 1
            if new_floor < self.number_of_floors:
                print(j)
        if new_floor > self.number_of_floors or new_floor < 0:
                print ('Такого этажа не существует')
#Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
#Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
#Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)