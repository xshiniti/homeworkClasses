class farmers_animals:
    name = ['animal', 'bird']
    paws = [2, 4]
    wings = ['Yes', 'None']
    size = ['big', 'small']

    def __init__(self, name, paws, wings, size):
        self.name = name
        self.paws = paws
        self.wings = wings
        self.size = size
        print(self.name, self.paws, self.wings, self.size)

    def __str__(self):
        return str({
            'name': self.name,
            'paws': self.paws,
            'wings': self.wings,
            'size': self.size,
        })


class Animal(farmers_animals):
    name_animal = ['Коровы', 'Козы', 'Овцы', 'Свиньи']

    def __init__(self, name_animal):
        self.name_animal = name_animal
        farmers_animals.__init__(self, name_animal, 4, 'None', 'big')


class Birds(farmers_animals):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        farmers_animals.__init__(self, name_bird, 2, 'Yes', 'small')


Cows = Animal('Коровы')
Goats = Animal('Козы')
Sheep = Animal('Овцы')
Pigs = Animal('Свиньи')

Ducks = Birds('Утки')
Chickens = Birds('Куры')
Geese = Birds('Гуси')

print('\n Класс Птицы:',
      '\n Утки: {}'.format(Ducks),
      '\n Куры: {}'.format(Chickens),
      '\n Гуси: {}'.format(Geese))

print('\n Класс Животные:',
      '\n Коровы: {}'.format(Cows),
      '\n Козы: {}'.format(Goats),
      '\n Овцы: {}'.format(Sheep),
      '\n Свиньи: {}'.format(Pigs))
