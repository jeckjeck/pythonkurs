
class Animal:
    num_of_animals = 0
    def __init__(self, name, age, species, gender):
        self.name = name
        self.age = age
        self.species = species
        self.gender = gender
        Animal.num_of_animals += 1

    def __repr__(self):
        """Formaterar strängarna så de blir så lik inputen som möjligt"""
        return "Zoo('{}', '{}', {}, '{}')".format(self.name, self.age, self.species, self.gender)

    def __str__(self):
        """Formaterar strängarna så outputen blir snyggare"""
        return  'Namn: ' +  self.name + '\n' + 'Ålder: ' + str(self.age) + '\n' + 'species: ' + self.species +\
                '\n' + 'Kön: ' + self.gender + '\n' + "-----------"

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSpecies(self):
        return self.species

    @staticmethod
    def clear_file():
        """Tömmer filen"""
        open('animal_list2.txt', 'w').close()

    def save_to_file(self):
        """Sparar till fil"""
        with open ('animal_list2.txt', 'a') as f:
            f.writelines(self.name + '\n' + str(self.age) + '\n' + self.species + '\n' + self.gender + '\n')

class Zoo(Animal):
    """Ärver ifrån Animalklassen"""
    def __init__(self, *args): # *args gör att init kan ta emot godtyckligt många argument
        super().__init__(*args) # detta gör så att funktionen ärver alla init argument ifrån klasserna över

    def add_animal(self):
        """Lägger till ett djur"""
        for animal in self.animals:
            if animal.name == self.name:
                print("Du har redan döpt något djur till", self.name)
                self.name = input("Vänligen ge djuret ett annat namn: ")
                print("------------")
        self.animals.append(self)

    def sell_animal(self):
        """Säljer ett djur"""
        if self in self.animals:
            self.animals.remove(self)


def is_string(line,string,isFalse=False):
    """funktionen testar om strängen är ett heltal eller sträng"""
    if isFalse == False:
        try:
            int(line)
        except ValueError as e:
            return line
        else:
            print(string, "is an integer, but it should be an string.")
            print("-----------")
    elif isFalse == True:
        try:
            int(line)
        except ValueError as e:
            print(e)
            print("-----------")
        else:
            return int(line)
    else:
        print("isFalse can only be True/False or empty.")
        raise ValueError


def load_animal_list(file):
    """Laddar in en fil med djur och deras attribut, testar även
    efter fel när filen läses in och lägger djuren i klassen Animal"""
    animal_list = []
    with open(file, 'r') as f:
        mylist = f.read().splitlines()
        for row_nr, line in enumerate(mylist):
            if row_nr % 4 == 0:
                name = is_string(line, "Name")
            elif (row_nr-1) % 4 == 0:
                age = is_string(line, "Age", isFalse=True)
                if age > 200:
                    print("Animal named", name, "Animal can't be more than 200 years.")
                    print("-----------")
            elif (row_nr-2) % 4 == 0:
                species = is_string(line, "Species")
            elif (row_nr-3) % 4 == 0:
                gender = is_string(line, "Gender")
                if gender not in ('Hane', 'Hona'):
                    print("Gender is:", gender)
                    print("gender can only be Hane or Hona.")
                Zoo(name, age, species, gender).add_animal()
            else:
                ("Något är fel med .txt filen")
        return animal_list

g
load_animal_list(file='animal_list.txt')
#print(Animal.num_of_animals)


#Animal('Jocke',13, 'frer', 'sdes').write_to_file_animal()
#Zoo('Jocke', 33, 'Alligator', 'Hane').add_animal()
Zoo('Jocke', 33, 'Papegoja', 'Hane').add_animal()
# Zoo('Bollen', 33, 'Papegoja', 'Hane').add_animal()
#Zoo('Jocke5', 33, 'Human', 'Hane').sell_animal()



# for animal in Zoo.animals:
#     if animal.name == "Jocke":
#          print(animal)

for count, animal in enumerate(sorted(Zoo.animals, key=Zoo.getAge, reverse=True)):
    #print(animal)
    print(repr(animal))
    if count == 0:
        Animal.clear_file()
    Animal.save_to_file(animal)
#Zoo.print_animals(Zoo.animals)

