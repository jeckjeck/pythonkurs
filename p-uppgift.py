# Titel: Djurpark
# Författare: Joakim Bäcklund
# Datum: 2017-06-28

# Detta är ett program som hjälper till att hålla reda på nyinköpta djur.
# Sorterar och rekommenderar djurägaren vad han borde köpa för parkens bästa.

# Program lagrar djur i en fil med namnet animal_list.txt mellan körningarna.
# Filen innehåller djurets namn, ålder, djurart och kön.
# Med följande format:
#
# Djurnamn
# Ålder
# Djurart
# Kön


class Animal:
    """"
    Klass för djur och deras attribut
    Klassen har metoder som fungerar som en datastruktur för djuret.


    :param name - sträng namnet på djuret
    :param age - ålder på djuret
    :param species - Vilken djurart djuret har
    :param gender - Vilket kön djuret har
    """

    def __init__(self, name, age, species, gender):
        self.name = name
        self.age = age
        self.species = species
        self.gender = gender

    def __repr__(self):
        """Formaterar strängarna till ett mer formellt format,
           så repr() blir så lik inputen som möjligt.
           Zoo("name", age, species, "gender")
        """
        return "Namn: " + self.name + "\n" + "Ålder: " + str(self.age) + "\n" + "Djurart: " + self.species + \
               "\n" + "Kön: " + self.gender + "\n"
        # return "Animals("{}", {}, "{}", "{}")".format(self.name, self.age, self.species, self.gender)

    def __str__(self):
        """Formaterar strängarna så outputen blir snyggare
           Namn: Skutt
           Ålder: 4
           Djurart: Antilop
           Kön: Hona
        """
        return "Namn: " + self.name + "\n" + "Ålder: " + str(self.age) + "\n" + "Djurart: " + self.species + \
               "\n" + "Kön: " + self.gender + "\n" + "-----------"

    def get_name(self):
        """returnerar djurnamn"""
        return self.name

    def get_age(self):
        """returnerar ålder på djur"""
        return self.age

    def get_species(self):
        """returnerar djurtart"""
        return self.species

    def get_gender(self):
        """returnerar kön på djur"""
        return self.gender


class Zoo(Animal):
    """Ärver metoder ifrån Animalklassen
    num_of_animals - räknare för nummer av djur på Zooet
    animals - tom lista där djuren som läggs till hamnar

    :attribut animals - lista för de tillagda djuren
    :attribut num_of_animals - räknare för antalet tilllagda djur
    """
    animals = []
    num_of_animals = 0

    def __init__(self, *args):  # *args gör att init kan ta emot godtyckligt många argument
        super().__init__(*args)  # detta gör så att funktionen ärver alla initiala argument ifrån klasserna ovanför

        # self.animals.append(self)

    def add_animal(self):
        """Lägger till ett djur
        kontrollerar så alla attribut
        är av rätt typ och antar rätt värde
        lägger sedan till djuret till en lista
        samt ökar num_of_animals med ett.
        """
        self.is_string(self.name, "Namn")
        self.is_string(self.age, "Ålder", is_false=True)
        self.is_string(self.species, "Djurart")
        self.is_string(self.gender, "Kön")

        for ani in self.animals:
            if ani.name == self.name:
                print("Du har redan döpt något djur till", self.name)
                self.name = input("Vänligen ge djuret ett annat namn: ")
                print("------------")
        if int(self.age) > 200:
            print("Djuret som heter", self.name, "kan inte vara mer än 200 år.")
            self.age = int(input("Vänligen skriv djurets riktiga ålder: "))
            print("-----------")
        if self.gender not in ("Hane", "Hona"):
            print("Kön är:", self.gender)
            print("Kön kan bara vara Hane eller hona.")
        self.animals.append(self)
        self.num_of_animals += 1

    def sell_animal(self):
        """Säljer ett djur"""
        if self in self.animals:
            self.animals.remove(self)
            self.num_of_animals -= 1

    @staticmethod
    def find_animal_by_name(name, animal_list):
        """Söker efter djur baserat på namn"""
        [print(animal) for animal in animal_list if name in animal.name]
        if name not in [animal.species for animal in animal_list]:
            print("------------")
            print("Tyvärr finns det inget djur med det namnet.")
            print("------------")

    @staticmethod
    def find_animal_by_age(animal_list, age):
        """Söker efter djur baserat på ålder"""
        [print(animal) for animal in animal_list if str(age) in str(animal.age)]
        if str(age) not in [str(animal.age) for animal in animal_list]:
            print("------------")
            print("Tyvärr finns det inget djur med den åldern.")
            print("------------")

    @staticmethod
    def find_animal_by_species(animal_list, species):
        """Söker efter djur baserat på djurart"""
        [print(animal) for animal in animal_list if species in animal.species]
        if species not in [animal.species for animal in animal_list]:
            print("------------")
            print("Tyvärr finns det inget av den djurarten ännu.")
            print("------------")

    @staticmethod
    def find_animal_by_gender(animal_list, gender):
        """Söker efter djur baserat på kön"""
        [print(animal) for animal in animal_list if gender in animal.gender]
        if gender not in [animal.gender for animal in animal_list]:
            print("------------")
            print("Tyvärr finns det inget djur med könet", gender, ", ännu")
            print("------------")

    @staticmethod
    def is_string(line, attribute, is_false=False):
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
                print(attribute, "är ett heltal, men det ska vara en sträng.")
                raise ValueError
        else:
            print("is_false kan bara vara True eller False.")
            raise ValueError

    @staticmethod
    def load_animal_list_from_file(filename):
        """Laddar in en fil med djur och deras attribut, testar även
        efter fel när filen läses in och lägger djuren i klassen Animal
        """
        with open(filename, "r") as f:
            mylist = f.read().splitlines()
            for row_nr, line in enumerate(mylist):
                if row_nr % 4 == 0:
                    name = line
                elif (row_nr - 1) % 4 == 0:
                    age = line
                elif (row_nr - 2) % 4 == 0:
                    species = line
                elif (row_nr - 3) % 4 == 0:
                    gender = line
                    if all([name, age, species, gender]):
                        Zoo(name, age, species, gender).add_animal()
                else:
                    print("Något är fel med .txt filen")

    @staticmethod
    def clear_file(filename):
        """funktion tömmer filen"""
        open(filename, "w").close()

    def save_to_file(self, filename):
        """Sparar till fil Skriver rad för rad."""
        with open(filename, "a") as f:
            f.writelines([self.name, str(self.age), self.species, self.gender])


def print_menu():
    """Skriver ut valmeny"""
    print("D  söka på Djur.")
    print("N  lägga till Nytt djur.")
    print("S  Sälja djur.")
    print("L  Lista alla Djur.")
    print("R  få Rekommendationer.")
    print("A  Avsluta.")


def choose():
    """Läser in och returnerar första bokstaven i användarens val.
    Omvandlar liten bokstav till stor.
    """
    choice = input("Vad vill du göra? ")
    return choice[0].upper()


def search_animal():
    """Menyval för vilket attribut och vad
    det ska vara för värde som det ska sökas på
     """
    print("Vilket attribut vill du söka på? \n"
          "D  söka på djurnamn. \n"
          "Å  söka på Ålder. \n"
          "A  söka på djurArt.\n"
          "K  söka på Kön. \n")
    choice2 = choose()

    if choice2 == "D":
        choice3 = input("Vilket namn? ")
        Zoo.find_animal_by_name(Zoo.animals, choice3)
    elif choice2 == "Å":
        choice3 = input("Vilken ålder? ")
        Zoo.find_animal_by_age(Zoo.animals, choice3)
    elif choice2 == "A":
        choice3 = input("Vilken djurart? ")
        Zoo.find_animal_by_species(Zoo.animals, choice3)
    elif choice2 == "K":
        choice3 = input("Vilket kön? ")
        Zoo.find_animal_by_gender(Zoo.animals, choice3)
    else:
        main()


def animal_choice():
    """Valmeny för djurattribut"""
    name = input("Vad heter djuret? ")
    age = input("Vilken ålder har djuret? ")
    species = input("Vilken djurart är djuret? ")
    gender = input("Vilken kön har djuret? Hane eller Hona. ")
    return name, age, species, gender


def add_animal():
    """Lägger till djur"""
    name, age, species, gender = animal_choice()
    Zoo(name, age, species, gender).add_animal()


def sell_animal():
    """Säljer djur"""
    name, age, species, gender = animal_choice()
    Zoo(name, age, species, gender).sell_animal()


def sorter(key, reverse=False):
    """ Skriver ut djur och sorterar på parametrarna
     som är de olika djurattribut i stigande (reverse = True)
     eller fallande (reverse = False) ordning
    """
    [print(animal) for animal in sorted(Zoo.animals, key=key, reverse=reverse)]


def print_all():
    """Skriver ut menyval för vilka attribut
     det ska sorteras på och vilken ordning
     """
    print("Vill du sortera på något attribut? "
          " N: Nej. \n"
          " A: nAmn. \n"
          " Å: Ålder. \n"
          " D: Djurart. \n"
          " G: Gå tillbaka. \n")
    choice2 = choose()
    if choice2 == "N":
        for animal in Zoo.animals:
            print(animal)
    elif choice2 == "Na":
        print("F: i Fallande ordning?\n"
              "S: i Stigande ordning \n")
        choice3 = choose()
        if choice3 == "F":
            sorter(Zoo.get_name)
        else:
            sorter(Zoo.get_name, reverse=True)
    elif choice2 == "Å":
        print("F: i Fallande ordning? \n"
              "S: i Stigande ordning \n")
        choice3 = choose()
        if choice3 == "F":
            sorter(Zoo.get_age)
        else:
            sorter(Zoo.get_age, reverse=True)

    elif choice2 == "D":
        print("F: i Fallande ordning? \n"
              "S: i Stigande ordning? \n")
        choice3 = choose()
        if choice3 == "F":
            sorter(Zoo.get_species)
        else:
            sorter(Zoo.get_species, reverse=True)
    else:
        main()


def get_unique_species():
    """returnerar en lista med de unika djurarterna som finns """
    unique_animal_list = []
    for x in Zoo.animals:
        unique_animal_list.append(x.species)
    unique_animal_list = list(set(unique_animal_list))
    return unique_animal_list


def species_counter(cond):
    """Funktionen skriver ut rekommendationer baserat på vad användare har för syfte"""
    unique_animal_list = get_unique_species()
    for ani in unique_animal_list:
        n = 0
        if cond == "breed":
            # Om anv. väljer breed, Skapas två variabler som fungerar som räknare senare.
            male = 0
            female = 0
        for animal in Zoo.animals:
            if animal.species == ani:
                n += 1
                string = ("borde köpas in en {0} av könet: {1}. "
                          "Det finns för närvarande {2} st. av den djurarten i parken. "
                          "Den eller de är av könet: {3}.") \
                    .format(str(ani), str({"Hona", "Hane"}.difference({animal.gender}))
                            .strip("{'}"), n, str(animal.gender))
                if cond == "breed":
                    if animal.gender == "Hane":
                        male += 1
                    elif animal.gender == "Hona":
                        female += 1
            if cond == "breed" and (male or female) and abs(male - female) > 1:
                # Om det finns fler hanar än honor eller tvärtom, samt att animal.gender
                # existerar, skrivs det djuret ut och vilket kön som bör köpas.
                print(string)

        if all([cond == "solo", string, n == 1]):
            print(string)

        if cond == "many":
            if n > 1:
                print("Du kan sälja en", ani + ". Det finns redan", n, "st. av typen.\n")


def rec():
    """Skriver ut en valmeny för vad anv. är intresserad
    av att få för sorts rekommendationer. Hänsyn tas till
    maxstorleken på djurparken.
    """
    print("Intresserad av att\n K: Köpa\n S: Sälja")
    choice = choose()
    if choice == "K":
        buy = True
    else:
        buy = False
    if buy:
        if Zoo.num_of_animals < 20:
            species_counter(cond="solo")
            species_counter(cond="breed")
        else:
            print("Du har inte plats för fler djur.")
    else:
        if Zoo.num_of_animals > 20:
            species_counter(cond="many")
        else:
            print("Du behöver inte sälja något djur. Då det fortfarande finns plats för fler.")


def main():
    Zoo.load_animal_list_from_file(filename="animal_list.txt")
    print("Välkommen till Djurparksprogrammet.")
    print_menu()
    choice = choose()
    while choice != "A":
        if choice == "D":
            search_animal()
        elif choice == "N":
            add_animal()
        elif choice == "S":
            sell_animal()
        elif choice == "L":
            print_all()
        elif choice == "R":
            rec()
        choice = choose()

    Zoo.clear_file("animal_list2.txt")
    [Zoo.save_to_file(animals, filename="animal_list2.txt") for animals in Zoo.animals]
    print("Välkommen åter!")

main()

# print(Zoo.animals)
# TODO fixa klasser, ta bort in argument från Zoo, instansmetoder av load! och tostring?
# TODO kodskelett
# TODO fixa så djurlistan fungerar?
# TODO maxtak för parken  fil?
