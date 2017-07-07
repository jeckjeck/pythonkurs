# Titel: Djurpark
# Författare: Joakim Bäcklund
# Datum: 2017-06-27

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
    Klassen har metoder som fungerar
    som en datastruktur för djuret.
    Dessa metoder används senare som key
    till sorteringsfunktionen
    utanför klasserna.

    Args:
        :param name: sträng namnet på djuret
        :param age:  ålder på djuret
        :param species:  Vilken djurart djuret har
        :param gender:  Vilket kön djuret har
    """

    def __init__(self, name, age, species, gender):
        self.name = name
        self.age = age
        self.species = species
        self.gender = gender

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

    """ Genom att sätta __repr__ samma som str,
    printas listorna ut i samma format som variabler.
    """
    __repr__ = __str__


class Zoo:
    """Klass för Djur på djurparken. Klassen sköter kontrollen av djur, funktioner för
    att lägga till djur, sälja djur, hitta djur och spara djurlistan.

    Args:
        :param filename: fil som kan läsas in.

    instansvariabel animals: -  tom lista för de tillagda djuren
    instansvariabel num_of_animals: - räknare för antalet tilllagda djur i djurparken
    """
    def __init__(self, filename=None):
        self.filename = filename
        self.animals = []
        self.max_space_for_animal_park = 0
        self.num_of_animals = 0

    def load_max_num_of_animals_from_file(self):
        with open("maxtak.txt", "r") as f:
            self.max_space_for_animal_park = int(f.read())

    def load_animal_list_from_file(self):
        """Laddar in en fil med djur och deras attribut, testar även
        efter fel när filen läses in och lägger djuren i klassen Animal
        """
        with open(self.filename, "r") as f:
            animals = f.read().splitlines()
            for row_nr, line in enumerate(animals):
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
        """funktionen testar om strängen består av bokstäver.

        Args:
            param attribute (str): djurattribut.
            param is_false (bool): default är False. Sätt till True
                        för att testa om strängen består av heltal.
        returns:
            ett heltal om man testar för heltal och det är sant, samma för sträng.
        """
        if is_false:
            try:
                int(attribute)
            except ValueError as e:
                print(e, "Ålder ska vara ett heltal.")
                age = input("Hur gammal är djuret? ")
                if int(age):
                    return int(age)
            else:
                return int(attribute)
        elif not is_false:
            try:
                int(attribute)
            except ValueError:
                return attribute
            else:
                print(attribute, "är ett heltal, men det ska vara en sträng.")
                return input("Vänligen skriv in det som en bokstav.")
        else:
            print("is_false kan bara vara True eller False.")

    def add_animal(self, animal):
        """
        Lägger till ett djur och kontrollerar så alla
        attribut är av rätt typ och antar rätt värde
        lägger sedan till djuret till en lista samt ökar
        num_of_animals med ett.

            param animal: är ett objekt av Animal-klassen.
        """
        self.is_string(animal.name)
        animal.age = self.is_string(animal.age, is_false=True)
        self.is_string(animal.species)
        self.is_string(animal.gender)
        for ani in self.animals:
            while ani.name == animal.name:
                print("Du har redan döpt något djur till", animal.name)
                animal.name = input("Vänligen ge djuret ett annat namn: ")
                print("------------")
        while 0 > int(animal.age) > 200:
            print("Djuret som heter", animal.name, "måste vara mellan 0-200 år.")
            animal.age = int(input("Vänligen skriv djurets riktiga ålder: "))
            print("-----------")
        while animal.gender not in ("Hane", "Hona"):
            print("Kön är:", animal.gender)
            print("Kön kan bara vara Hane eller Hona.")
            animal.gender = input("Vänligen skriv djurets riktiga kön: ")
            print("-----------")
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
        """Söker efter djur baserat på djurets ålder
        Returnerar en lista med alla djur som har
        åldern som specificeras i argumentet.
        """
        animal_list = []
        for animal in self.animals:
            if age in animal.age:
                animal_list.append(animal)
        return animal_list

    def find_animal_by_species(self, species):
        """Söker efter djur baserat på djurets art.
        Returnerar en lista med alla djur med som tillhör
        arten som specificeras i argumentet.
        """
        animal_list = []
        for animal in self.animals:
            if species in animal.species:
                animal_list.append(animal)
        return animal_list

    def find_animal_by_gender(self, gender):
        """Söker efter djur baserat på djurets kön
        Returnerar en lista med alla djur som har
        könet som specificeras i argumentet.
        """
        animal_list = []
        for animal in self.animals:
            if gender in animal.gender:
                animal_list.append(animal)
        return animal_list

    def save_animals_to_file(self, filename):
        """Sparar till fil Skriver rad för rad."""
        with open(filename, "w") as f:
            for animal in self.animals:
                f.writelines([animal.name, '\n', str(animal.age), '\n', animal.species, '\n', animal.gender, '\n'])


def print_menu():
    """Skriver ut valmeny"""
    print("D  söka på Djur. \n"
          "K  Köpa in nytt djur.\n"
          "S  Sälja djur.\n"
          "L  Lista alla Djur.\n"
          "R  få Rekommendationer.\n"
          "A  Avsluta.")


def choose():
    """returnerar användarens val."""
    return input("Vad vill du göra? ")



def search_animal(zoo):
    """Menyval för vilket attribut och vad
    det ska vara för värde som det ska sökas på
     """
    print("Vilket attribut vill du söka på? \n"
          "D  söka på djurnamn. \n"
          "Å  söka på Ålder. \n"
          "A  söka på djurArt.\n"
          "K  söka på Kön. \n"
          " G: Gå tillbaka. \n")
    attribute = choose()
    if attribute == "G":
        main(back=True)
    if attribute == "D":
        name = input("Vilket namn? ")
        animal = zoo.find_animal_by_name(name)
        if animal:
            print(animal)
        else:
            print("Tyvärr finns det inget djur med det namnet.")
    elif attribute == "Å":
        age = input("Vilken ålder? ")
        animal_list = zoo.find_animal_by_age(age)
        if animal_list:
            [print(animal) for animal in animal_list]
        else:
            print("Tyvärr finns det inget djur med den åldern.")
    elif attribute == "A":
        species = input("Vilken djurart? ")
        animal_list = zoo.find_animal_by_species(species)
        if animal_list:
            [print(animal) for animal in animal_list]
        else:
            print("Tyvärr finns ingen av den djurarten ännu.")
    elif attribute == "K":
        gender = input("Vilket kön? ")[0].upper()
        animal_list = zoo.find_animal_by_gender(gender)
        if animal_list:
            [print(animal) for animal in animal_list]
        else:
            print("Tyvärr finns det inget djur med könet", gender, "ännu.")
    else:
        main()


def animal_attribute_choice():
    """Valmeny för djurattribut"""
    name = None
    age = None
    species = None
    gender = None
    while not name:
        name = input("Vad vill du djuret ska heta? ")
    while not age:
        age = input("Vilken ålder har djuret? ")
    while not species:
        species = input("Vilken djurart tillhör djuret? ")
    while not gender:
        gender = input("Vilken kön har djuret? Hane eller Hona. ").title()
    return name, age, species, gender



def add_animal(zoo):
    """Lägger till djur"""
    name, age, species, gender = animal_attribute_choice()
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

        param reverse: True eller i fallande (reverse = False) ordning
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
    attr_choice = choose()
    if attr_choice == "I":
        [print(x) for x in zoo.animals]
    elif attr_choice == "N":
        print("F: i Fallande ordning?\n"
              "S: i Stigande ordning \n")
        order = choose()
        if order == "F":
            sorter(zoo, Animal.get_name)
        else:
            sorter(zoo, Animal.get_name, reverse=True)
    elif attr_choice == "Å":
        print("F: i Fallande ordning? \n"
              "S: i Stigande ordning \n")
        order = choose()
        if order == "F":
            sorter(zoo, Animal.get_age)
        else:
            sorter(zoo, Animal.get_age, reverse=True)

    elif attr_choice == "D":
        print("F: i Fallande ordning? \n"
              "S: i Stigande ordning? \n")
        order = choose()
        if order == "F":
            sorter(zoo, Animal.get_species)
        else:
            sorter(zoo, Animal.get_species, reverse=True)
    elif attr_choice == "G":
        main(back=True)


def get_unique_species(zoo):
    """returnerar en lista med de unika djurarterna som finns """
    unique_animal_list = []
    for animal in zoo.animals:
        unique_animal_list.append(animal.species)
        # Projektion på djurlistan, tar fram de unika djurarterna
        # och stoppar dem i en ny lista

    return list(set(unique_animal_list))


def species_counter(zoo, cond):
    """Funktionen skriver ut rekommendationer baserat på vad användare har för syfte

    param cond: om syftet är att  leta efter djur som är ensamma (solo),många (many)
    eller om syftet är avla (breed)

    """
    unique_animal_list = get_unique_species(zoo)
    for ani in unique_animal_list:
        n = 0
        if cond == "breed":
            # Om anv. väljer breed, Skapas två variabler som fungerar som räknare senare.
            male = 0
            female = 0
        for animal in zoo.animals:
            if animal.species == ani:
                n += 1
                string = ("Det finns för närvarande {2} st. av typen {0} i parken. "
                          "Den eller de är av könet: {3}. För att avla borde det köpas in en {1}. \n")\
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
        if cond == "many" and n > 1:
            print("Du kan sälja en", ani + ". Det finns redan", n, "st. av den typen.\n")


def rec_animals(zoo):
    """Skriver ut en valmeny för vad anv. är intresserad
    av att få för sorts rekommendationer.
    Och därefter listas rekommendationer. Hänsyn tas till
    maxstorleken på djurparken.
    """
    print("Intresserad av att\n K: Köpa\n S: Sälja\n G: Gå tillbaka")
    user_choice = choose()
    buy = False
    if user_choice == "K":
        buy = True
    if user_choice == "G":
        main(back=True)
    if buy:
        if zoo.num_of_animals < zoo.max_space_for_animal_park:
            species_counter(zoo, cond="solo")
            species_counter(zoo, cond="breed")
        else:
            print("Du har inte plats för fler djur.")
    else:
        if zoo.num_of_animals >= zoo.max_space_for_animal_park:
            species_counter(zoo, cond="many")
        else:
            print("Du behöver inte sälja något djur. Då det fortfarande finns plats för fler.")


def main(back=False):
    file = "animal_list.txt"
    zoo = Zoo(file)
    zoo.load_animal_list_from_file()
    zoo.load_max_num_of_animals_from_file()
    if back:
        print("\n\nVad vill du göra härnäst?")
    if not back:
        print("Välkommen till Djurparksprogrammet.")
    print_menu()
    user_main_choice = choose()
    while user_main_choice != "A":
        if user_main_choice == "D":
            search_animal(zoo)
        elif user_main_choice == "K":
            add_animal(zoo)
        elif user_main_choice == "S":
            sell_animal(zoo)
        elif user_main_choice == "L":
            print_all(zoo)
        elif user_main_choice == "R":
            rec_animals(zoo)
            user_main_choice = choose()

    zoo.save_animals_to_file(file)
    print("Välkommen åter!")

main()


# TODO Felhantering
# När jag matade in A vid “vad vill du göra?” som kom upp efter att jag listat djur så skriver programmet ut “välkommen åter!” och sedan “Vad vill du göra?” igen. När jag skriver in A en andra gång stängs programmet ner.
