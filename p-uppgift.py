# Titel: Djurpark
# Författare: Joakim Bäcklund
# Datum: 2017-06-22

# Detta är ett program som hjälper till att hålla reda på nyinköpta djur.

# Program lagrar djur i en fil med namnet animal_list.txt
# Mellan körningarna. Filen innehåller djurets namn, ålder, djurart och kön.
# Med följande format:
#
# Djurnamn
# Ålder
# Djurart
# Kön


class Animal:
    """"
    Klass för djur och deras attribut
    Klassen har metoder som kan skapa, tabort, hämta relevant information om djuren.


    :param name - sträng namnet på djuret
    :param age - ålder på djuret
    :param species - Vilken djurart djuret har
    :param gender - Vilket kön djuret har
    :attribut num_of_animals - räknare för antalet tilllagda djur
    """

    def __init__(self, name, age, species, gender):
        self.name = name
        self.age = age
        self.species = species
        self.gender = gender

    def __repr__(self):
        """Formaterar strängarna till ett mer formellt format,
           så repr() blir så lik inputen som möjligt.
           Zoo('name', age, species, 'gender')"""
        return 'Namn: ' + self.name + '\n' + 'Ålder: ' + str(self.age) + '\n' + 'Djurart: ' + self.species + \
               '\n' + 'Kön: ' + self.gender + '\n'
        # return "Animals('{}', {}, '{}', '{}')".format(self.name, self.age, self.species, self.gender)

    def __str__(self):
        """Formaterar strängarna så outputen blir snyggare
           Namn: Skutt
           Ålder: 4
           Djurart: Antilop
           Kön: Hona
        """
        return 'Namn: ' + self.name + '\n' + 'Ålder: ' + str(self.age) + '\n' + 'Djurart: ' + self.species +\
               '\n' + 'Kön: ' + self.gender + '\n' + "-----------"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_species(self):
        return self.species

    def get_gender(self):
        return self.gender


class Zoo(Animal):
    """Ärver metoder ifrån Animalklassen
    num_of_animals - räknare för nummer av djur på Zooet
    animals - tom lista för
    """
    animals = []
    num_of_animals = 0

    def __init__(self, *args):     # *args gör att init kan ta emot godtyckligt många argument
        super().__init__(*args)    # detta gör så att funktionen ärver alla init argument ifrån klasserna över

        Zoo.num_of_animals += 1
        #self.animals.append(self)

    def add_animal(self):
        """Lägger till ett djur"""
        for ani in self.animals:
            if ani.name == self.name:
                print("Du har redan döpt något djur till", self.name)
                self.name = input("Vänligen ge djuret ett annat namn: ")
                print("------------")
        self.animals.append(self)

    def sell_animal(self):
        """Säljer ett djur"""
        if self in self.animals:
            self.animals.remove(self)

    @staticmethod
    def find_animal_by_name(name, animal_list):
        [print(animal) for animal in animal_list if name in animal.name]
        if name not in [animal.species for animal in animal_list]:
            print("------------")
            print("Tyvärr finns det inget djur med det namnet.")
            print("------------")
    @staticmethod
    def find_animal_by_age(animal_list, age):
        [print(animal) for animal in animal_list if str(age) in str(animal.age)]
        if str(age) not in [str(animal.age) for animal in animal_list]:
                print("------------")
                print("Tyvärr finns det inget djur med den åldern.")
                print("------------")
    @staticmethod
    def find_animal_by_species(animal_list, species):
        [print(animal) for animal in animal_list if species in animal.species]
        if species not in [animal.species for animal in animal_list]:
                print("------------")
                print("Tyvärr finns det inget av den djurarten ännu.")
                print("------------")

    @staticmethod
    def find_animal_by_gender(animal_list, gender):
        [print(animal) for animal in animal_list if gender in animal.gender]
        if gender not in [animal.gender for animal in animal_list]:
            print("------------")
            print("Tyvärr finns det inget djur med könet", gender, ", ännu")
            print("------------")

    @classmethod
    def is_string(cls, line, attribute, is_false=False):
        """funktionen testar om strängen är ett heltal eller sträng

        :param line är en sträng.
        :param attribute är vilket attribut det är fel på, bara till för utskrift.
        :param is_false boolean typ, default är False. Sätt till True
                        för att testa om det är ett en heltal.
        :returnerar ett heltal om man testar för heltal och det är sant, samma för sträng.
        """
        if is_false:
            try:
                int(line)
            except ValueError as e:
                print(e)
                print("-----------")
            else:
                return int(line)
        elif not is_false:
            try:
                int(line)
            except ValueError:
                return line
            else:
                print(attribute, "is an integer, but it should be an string.")
                raise ValueError
        else:
            print("is_false can only be True/False or empty.")
            raise ValueError

    @classmethod
    def load_animal_list_from_file(cls, filename):
        """Laddar in en fil med djur och deras attribut, testar även
        efter fel när filen läses in och lägger djuren i klassen Animal
        """
        with open(filename, 'r') as f:
            mylist = f.read().splitlines()
            for row_nr, line in enumerate(mylist):
                if row_nr % 4 == 0:
                    name = cls.is_string(line, "Name")
                elif (row_nr - 1) % 4 == 0:
                    age = cls.is_string(line, "Age", is_false=True)
                    if age > 200:
                        print("Animal named", name, "Animal can't be more than 200 years.")
                        age = int(input("Please enter the correct age"))
                        print("-----------")
                elif (row_nr - 2) % 4 == 0:
                    species = cls.is_string(line, "Species")
                elif (row_nr - 3) % 4 == 0:
                    gender = cls.is_string(line, "Gender")
                    if gender not in ('Hane', 'Hona'):
                        print("Gender is:", gender)
                        print("gender can only be Hane or Hona.")
                    Zoo(name, age, species, gender).add_animal()
                else:
                    print("Något är fel med .txt filen")

    @staticmethod
    def clear_file(filename):
        """funktion ömmer filen"""
        open(filename, 'w').close()

    def save_to_file(self, filename):
        """Sparar till fil"""

        with open(filename, 'a') as f:
                f.writelines(self.name + '\n' + str(self.age) + '\n' + self.species + '\n' + self.gender + '\n')






Zoo.load_animal_list_from_file(filename='animal_list.txt')
print(Zoo.num_of_animals)


# Animal('Jocke',13, 'frer', 'sdes').write_to_file_animal()
# Zoo('Jocke', 33, 'Alligator', 'Hane').add_animal()
Zoo('Jocke4', 33, 'Papegoja', 'Hane').add_animal()
# Zoo('Bollen', 33, 'Papegoja', 'Hane').add_animal()
# Zoo('Jocke5', 33, 'Human', 'Hane').sell_animal()

# for animal in Zoo.animals:
#     if animal.name == "Jocke":
#          print(animal)

# for count, animal in enumerate(sorted(Zoo.animals, key=Animal.get_age, reverse=True)):
#     print(animal)
#     print(repr(animal))
#     if count == 0:
#         Zoo.clear_file('animal_list2.txt')
#     Zoo.save_to_file(animal, filename='animal_list2.txt')



# Zoo.find_animal_by_gender(sorted(Zoo.animals, key=Animal.get_age, reverse=True), gender="Hona")
# Zoo.find_animal_by_species(sorted(Zoo.animals, key=Animal.get_age, reverse=True), species="Antilop")
#print(Zoo.animals)
#Zoo.find_animal_by_species(Zoo.animals, species="Gorilla")

INDENT = "  " # Tomma tecken i början av indragna rader

def print_menu():
    print(INDENT + "D  söka på Djur.")
    print(INDENT + "Å  söka på Ålder.")
    print(INDENT + "D  söka på Djurart.")
    print(INDENT + "K  söka på Kön.")
    print(INDENT + "N  lägga till Nytt djur.")
    print(INDENT + "B  ta Bort djur.")
    print(INDENT + "A  lista Alla Djur.")
    print(INDENT + "S  Sluta.")

# Läser in och returnerar första bokstaven i användarens val.
# Omvandlar liten bokstav till stor.
def choose():
    choice = input("Vad vill du göra? ")
    return choice[0].upper()

# Söker på titel.
def search_title(Zoo):
    title = input("Vilken djurart vill du söka efter? ")
    Zoo.find_animal_by_species(Zoo.animals, title)

def print_all(Zoo):
    choice = input("Vill du sortera på något attribut? N: Nej \n N: Namn \n Å: Ålder \n D: Djurart \n G: Gå tillbaka ")
    if choice == "N":
        print(Zoo.animals)
    elif choice == "Na":
        print(sorted(Zoo.animals, key=Zoo.name))
    elif choice == "Å":
        print(sorted(Zoo.animals, key=Zoo.age))
    elif choice == "D":
        print(sorted(Zoo.animals, key=Zoo.species))
    else:
        main()

# Söker på författare.
# def search_author(catalog):
#     author = input("Vad vill du söka efter: 1: Djur ")
#     book_list = catalog.find_author(author)
#     if len(book_list) == 0:
#         print(INDENT + "Hittade inga böcker av den författaren.")
#     else:
#         print(INDENT + "Hittade " + str(len(book_list)) + " böcker")
#         for book in book_list:
#             print(INDENT + book)




def main():
    print("Välkommen till Djurparksprogrammet.")
    print_menu()
    choice = choose();
    while choice != "S":
        if choice == "D":
            search_title(Zoo)
        elif choice == "A":
            print_all(Zoo)
        choice = choose()

    Zoo.clear_file('animal_list2.txt')
    for animals in Zoo.animals:
        Zoo.save_to_file(animals, filename='animal_list2.txt')


    print(INDENT + "Välkommen åter!")


print(Zoo.animals)