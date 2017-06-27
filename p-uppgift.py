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
           Animal("name", age, species, "gender")
        """
        return "Animals({0}, {1}, {2}, {3})".format(self.name, self.age, self.species, self.gender)

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
        return int(self.age)

    def get_species(self):
        """returnerar djurtart"""
        return self.species

    def get_gender(self):
        """returnerar kön på djur"""
        return self.gender


class Zoo:
    """Klass för Djur på djurparken. Klassen sköter kontrollen av djur, funktioner för
    att lägga till djur, sälja djur, hitta djur och spara djurlistan.


    :param filename - fil som kan läsas in.
    :instansvariabel animals -  tom lista för de tillagda djuren
    :instansvariabel num_of_animals - räknare för antalet tilllagda djur i djurparken
    """
    def __init__(self, filename=None):
        self.filename = filename
        self.animals = []
        self.max = None
        self.num_of_animals = 0

    def load_max_num_of_animals_from_file(self):
        with open("maxtak.txt", "r") as f:
            self.max = int(f.read())

    def load_animal_list_from_file(self):
        """Laddar in en fil med djur och deras attribut, testar även
        efter fel när filen läses in och lägger djuren i klassen Animal
        """
        with open(self.filename, "r") as f:
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
                        animal = Animal(name, age, species, gender)
                        self.add_animal(animal)
                else:
                    print("Något är fel med .txt filen")

    @staticmethod
    def is_string(attribute, is_false=False):
        """funktionen testar om strängen är ett heltal eller sträng

        :param attribute är en sträng.
        :param is_false boolean typ, default är False. Sätt till True
                        för att testa om det är ett en heltal.
        :returnerar ett heltal om man testar för heltal och det är sant, samma för sträng.
        """
        if is_false:
            try:
                int(attribute)
            except ValueError as e:
                print(e, "Ålder ska vara en ett heltal och inte en textsträng.")
                print("-----------")
            else:
                return int(attribute)
        elif not is_false:
            try:
                int(attribute)
            except ValueError:
                return attribute
            else:
                print(attribute, "är ett heltal, men det ska vara en sträng.")
                raise ValueError
        else:
            print("is_false kan bara vara True eller False.")
            raise ValueError

    def add_animal(self, animal):
        """
        Lägger till ett djur och kontrollerar så alla
        attribut är av rätt typ och antar rätt värde
        lägger sedan till djuret till en lista samt ökar
        num_of_animals med ett.

        : param animal -- är ett objekt av Animal-klassen.
        """
        self.is_string(animal.name)
        self.is_string(animal.age, is_false=True)
        self.is_string(animal.species)
        self.is_string(animal.gender)
        for ani in self.animals:
            if ani.name == animal.name:
                print("Du har redan döpt något djur till", animal.name)
                animal.name = input("Vänligen ge djuret ett annat namn: ")
                print("------------")
        if int(animal.age) > 200:
            print("Djuret som heter", animal.name, "kan inte vara mer än 200 år.")
            animal.age = int(input("Vänligen skriv djurets riktiga ålder: "))
            print("-----------")
        if animal.gender not in ("Hane", "Hona"):
            print("Kön är:", animal.gender)
            print("Kön kan bara vara Hane eller hona.")
        self.animals.append(animal)
        self.num_of_animals += 1

    def sell_animal(self, name):
        """Säljer ett djur"""
        for animal in self.animals:
            if name == animal.name:
                self.animals.remove(animal)
                self.num_of_animals -= 1

    def find_animal_by_name(self, name):
        """Söker efter djur baserat på djurets namn"""
        for animal in self.animals:
            if name in animal.name:
                return animal
        return None

    def find_animal_by_age(self, age):
        """Söker efter djur baserat på djurets ålder"""
        for animal in self.animals:
            if age in animal.age:
                return animal
        return None

    def find_animal_by_species(self, name):
        """Söker efter djur baserat på djurets art"""
        for animal in self.animals:
            if name in animal.name:
                return animal
        return None

    def find_animal_by_gender(self, gender):
        """Söker efter djur baserat på djurets kön"""
        for animal in self.animals:
            if gender in animal.gender:
                return animal
        return None

    def save_to_file(self, filename):
        """Sparar till fil Skriver rad för rad."""
        with open(filename, "w") as f:
            for animal in self.animals:
                f.writelines([animal.name, '\n', animal.age, '\n', animal.species, '\n', animal.gender, '\n'])


def print_menu():
    """Skriver ut valmeny"""
    print("D  söka på Djur.")
    print("N  lägga till Nytt djur.")
    print("S  Sälja djur.")
    print("L  Lista alla Djur.")
    print("R  få Rekommendationer.")
    print("A  Avsluta.")


def choose():
    """returnerar användarens val."""
    choice = input("Vad vill du göra? ")
    return choice


def search_animal(zoo):
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
        name = input("Vilket namn? ")
        animal = zoo.find_animal_by_name(name)
        if animal:
            print(animal)
        else:
            print("Tyvärr finns det inget djur med det namnet.")
    elif choice2 == "Å":
        age = input("Vilken ålder? ")
        animal = zoo.find_animal_by_age(age)
        if animal:
            print(animal)
        else:
            print("Tyvärr finns det inget djur med den åldern.")
    elif choice2 == "A":
        species = input("Vilken djurart? ")
        animal = zoo.find_animal_by_species(species)
        if animal:
            print(animal)
        else:
            print("Tyvärr finns ingen av den djurarten ännu.")
    elif choice2 == "K":
        gender = input("Vilket kön? ")
        animal = zoo.find_animal_by_gender(gender)
        if animal:
            print(animal)
        else:
            print("Tyvärr finns det inget djur med könet", gender, "ännu.")
    else:
        main()


def animal_choice():
    """Valmeny för djurattribut"""
    name = input("Vad heter djuret? ")
    age = input("Vilken ålder har djuret? ")
    species = input("Vilken djurart är djuret? ")
    gender = input("Vilken kön har djuret? Hane eller Hona. ")
    return name, age, species, gender


def add_animal(zoo):
    """Lägger till djur"""
    name, age, species, gender = animal_choice()
    animal = Animal(name, age, species, gender)
    zoo.add_animal(animal)


def sell_animal(zoo):
    """Säljer djur"""
    name = input("Vad heter djuret? ")
    zoo.sell_animal(name)


def sorter(zoo, key, reverse=False):
    """
    Skriver ut djur och sorterar på olika attributena med hjälp
    av parametern key som är metoder i Animalklassen i stigande
    (reverse = True) eller i fallande (reverse = False) ordning
    """
    [print(animal) for animal in sorted(zoo.animals, key=key, reverse=reverse)]


def print_all(zoo):
    """Skriver ut menyval för vilka attribut
     det ska sorteras på och i vilken ordning
     """
    print("Vill du sortera efter något attribut? \n"
          " I: Inget. \n"
          " N: Namn. \n"
          " Å: Ålder. \n"
          " D: Djurart. \n"
          " G: Gå tillbaka. \n")
    choice2 = choose()
    if choice2 == "I":
        [print(x) for x in zoo.animals]
    elif choice2 == "N":
        print("F: i Fallande ordning?\n"
              "S: i Stigande ordning \n")
        choice3 = choose()
        if choice3 == "F":
            sorter(zoo, Animal.get_name)
        else:
            sorter(zoo, Animal.get_name, reverse=True)
    elif choice2 == "Å":
        print("F: i Fallande ordning? \n"
              "S: i Stigande ordning \n")
        choice3 = choose()
        if choice3 == "F":
            sorter(zoo, Animal.get_age)
        else:
            sorter(zoo, Animal.get_age, reverse=True)

    elif choice2 == "D":
        print("F: i Fallande ordning? \n"
              "S: i Stigande ordning? \n")
        choice3 = choose()
        if choice3 == "F":
            sorter(zoo, Animal.get_species)
        else:
            sorter(zoo, Animal.get_species, reverse=True)
    else:
        main()


def get_unique_species(zoo):
    """returnerar en lista med de unika djurarterna som finns """
    unique_animal_list = []
    for animal in zoo.animals:
        unique_animal_list.append(animal.species)
        # Projektion på sig själv, tar fram de unika värdena
        # och stoppar dem i en ny lista
        return list(set(unique_animal_list))


def species_counter(zoo, cond):
    """Funktionen skriver ut rekommendationer baserat på vad användare har för syfte"""
    unique_animal_list = get_unique_species(zoo)
    for species in unique_animal_list:
        n = 0
        if cond == "breed":
            # här skapas två variabler som fungerar som räknare senare.
            male = 0
            female = 0
        for animal in zoo.animals:
            if animal.species ==species:
                n += 1
                # strängen som printas vid rekommendationer skapas redan här
                # då den används på två olika ställen.
                string = ("borde köpas in en {0} av könet: {1}. "
                          "Det finns för närvarande {2} st. av den djurarten i parken. "
                          "Den eller de är av könet: {3}.") \
                    .format(str(species), str({"Hona", "Hane"}.difference({animal.gender}))
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
                print("Du kan sälja en", species + ". Det finns redan", n, "st. av typen.\n")


def rec(zoo):
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
        if zoo.num_of_animals < zoo.max:
            species_counter(zoo, cond="solo")
            species_counter(zoo, cond="breed")
        else:
            print("Du har inte plats för fler djur.")
    else:
        if zoo.num_of_animals > zoo.max:
            species_counter(zoo, cond="many")
        else:
            print("Du behöver inte sälja något djur. Då det fortfarande finns plats för fler.")


def main():
    file = "animal_list.txt"
    zoo = Zoo(file)
    zoo.load_animal_list_from_file()
    zoo.load_max_num_of_animals_from_file()

    print("Välkommen till Djurparksprogrammet.")
    print_menu()
    choice = choose()
    while choice != "A":
        if choice == "D":
            search_animal(zoo)
        elif choice == "N":
            add_animal(zoo)
        elif choice == "S":
            sell_animal(zoo)
        elif choice == "L":
            print_all(zoo)
        elif choice == "R":
            rec(zoo)
        choice = choose()

    zoo.save_to_file(file)
    print("Välkommen åter!")

main()
