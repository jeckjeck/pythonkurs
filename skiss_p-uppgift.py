
class Animal:
    num_of_animals = 0

    def __init__(self, name, age, art, gender):
        self.name = name
        self.age = age
        self.art = art
        self.gender = gender
        Animal.num_of_animals += 1

    def save_animal(self):
        with open ('animal_list.txt', 'a') as f:
            f.writelines(self.name + '\n' + str(self.age) + '\n' + self.art + '\n' + self.gender + '\n')

class Zoo:
    animals = []
    def add_animal(self, ani):
        if ani not in self.animals:
            self.animals.append(ani)

    def remove_animal(self, ani):
        if ani in self.animals:
            self.animals.append(ani)

    def print_animals(self):
        for animal in self.animals:
            print(animal)



Animal('Bebbe', 5, 'Gorilla', 'Hona').save_animal()
Animal('Bollen',2, 'Panda', 'Hane').save_animal()
Animal('Cosmos',7, 'Surikat', 'Hane').save_animal()
Animal('Diddi',3, 'Alligator', 'Hane').save_animal()
Animal('Skutt',4, 'Antilop', 'Hona').save_animal()
Animal('Wingo',12, 'Alligator', 'Hona').save_animal()
Animal('Marcello',6, 'Elg', 'Hane').save_animal()
Animal('Flax',15, 'Papegoja', 'Hane').save_animal()
Animal('Sipper',12, 'Gnu', 'Hona').save_animal()



animal_1 = {'name': 'Bebbe', 'age':  5, 'art': 'Gorilla', 'gender': 'Hona'}
animal_2 = {'name': 'Bollen', 'age': 2, 'art': 'Panda', 'gender': 'Hane'}
animal_3 = {'name': 'Cosmos', 'age': 7, 'art': 'Surikat', 'gender': 'Hane'}
animal_4 = {'name': 'Diddi','age': 3, 'art':' Alligator', 'gender': 'Hane'}
animal_5 = {'name': 'Skutt', 'age': 4, 'art': 'Antilop', 'gender': 'Hona'}
animal_6 = {'name': 'Wingo', 'age': 12, 'art': 'Alligator', 'gender':'Hona'}
animal_7 = {'name': 'Marcello','age': 6, 'art': 'Elk', 'gender': 'Hane'}
animal_8 = {'name': 'Flax', 'age': 15, 'art': 'Papegoja', 'gender': 'Hane'}
animal_9 = {'name': 'Sipper','age': 12, 'art': 'Gnu', 'gender': 'Hona'}

animal_list = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9]




#np.save("my_dict.npy", [x for x in animal_list])

#dict_arr = np.load("my_dict.npy")

#new_list =[x for x in dict_arr]

# for animal in new_list:
#      print("\nAnimal name:", animal['name'], "\nAge:", animal['age'], "\nArt:", animal['art'], "\nGender:", animal['gender'])

#print([animal for animal in sorted(new_list) if animal['age'] > 6])
#
# dict = [animal for animal in new_list]


#print(animal_1.name)
#Zoo.add_animal(ani=animal_1.name)
# Animal.add_animal(animal_2)
# Animal.add_animal(animal_3)
# Animal.add_animal(animal_4)
# Animal.add_animal(animal_5)
# Animal.add_animal(animal_6)
# Animal.add_animal(animal_7)
# Animal.add_animal(animal_8)
# Animal.add_animal(animal_9)

# print(Animal.num_of_animals)

#print(Animal.get_name(animal_1))


animal_1 = ['Bebbe', 5,'Gorilla','Hona']
animal_2 = ['Bollen',2, 'Panda', 'Hane']
animal_3 = ['Cosmos',7, 'Surikat', 'Hane']
animal_4 = ['Diddi',3, 'Alligator', 'Hane']
animal_5 = ['Skutt',4, 'Antilop', 'Hona']
animal_6 = ['Wingo',12, 'Alligator', 'Hona']
animal_7 = ['Marcello',6, 'Älg', 'Hane']
animal_8 = ['Flax',15, 'Papegoja', 'Hane']
animal_9 = ['Sipper',12, 'Gnu', 'Hona']

animal_list = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9]

with open('animal_nest_list.txt', 'w') as f:
    f.writelines([str(x) for x in animal_list])

with open('animal_nest_list.txt', 'r') as f:
    animal_list = f.readlines()

