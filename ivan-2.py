class House():
    """ Описание класса House """
    def __init__(self, street, number):
        """ Здесь задаются свойства дома """
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """ Будет выводит сообщение, что дом на улице построен """
        print(f"Дом на улице {self.street} под номером {self.number} построен в срок!")
    def age_of_house(self, year):
        """ Определяем возраст дома """
        self.age += year

# # Создадим экземляры домов на основе класса House
# House1 = House('Московская', 20)
# House2 = House('Московская', 21)
# # Проверяем адрес первого дома
# print(House1.street)
# # ОБращаемся к методу в классе
# House2.build()
# # Задаем года
# House2.age_of_house(5)
# print("Восзраст дома House2 состовляет " + str(House2.age) + " лет!")

# ######################################
# Наследование
class ProsHouse(House):
    """ Дома на проспекте. Этот дочерной класс наследует все свойства класса House """
    def __init__(self, pros, number):
        super().__init__(self, number)
        self.pros = pros

PrH1 = ProsHouse("Ленина", 5)
print(PrH1.pros)
