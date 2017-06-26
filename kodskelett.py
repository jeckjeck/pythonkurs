# Titel: Djurpark
# Författare: Joakim Bäcklund
# Datum: 2017-06-27

# Detta är ett enkelt program som hjälper till att hålla reda på nyinköpta djur.
# Program lagrar djur i en fil med namnet animal_list.txt mellan körningarna.



class Animal:
    """"
    Klass för djur och deras attribut.
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
        """Formaterar strängarna till ett mer formellt format"""
        return

    def __str__(self):
        """Formaterar strängarna så outputen blir snyggare"""
        return

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
        """läser in djurets maxantal från textfil"""

    def load_animal_list_from_file(self):
        """läser in en textfil"""
        return

    def add_animal(self, animal):
        """
        Lägger till ett djur och kontrollerar så alla
        attribut är av rätt typ och antar rätt värde
        lägger sedan till djuret till en lista samt ökar
        num_of_animals med ett.

        : param animal -- är ett objekt av Animal-klassen.
        """
        return

    def sell_animal(self, name):
        """Säljer ett djur"""
        return

    def find_animal_by_name(self, name):
        """Söker efter djur baserat på djurets namn"""
        return

    def find_animal_by_age(self, age):
        """Söker efter djur baserat på djurets ålder"""
        return

    def find_animal_by_species(self, name):
        """Söker efter djur baserat på djurets art"""
        return

    def find_animal_by_gender(self, gender):
        """Söker efter djur baserat på djurets kön"""
        return

    @staticmethod
    def is_string(attribute, is_false=False):
        """funktionen testar om strängen är ett heltal eller textsträng

        :param attribute är en sträng.
        :param is_false boolean typ, default är False. Sätt till True
                        för att testa om det är ett en heltal.
        :returnerar ett heltal om man testar för heltal och det är sant, samma för sträng.
        """
        return

    def save_to_file(self, filename):
        """Sparar till fil Skriver rad för rad."""
        return

def print_menu():
    """Skriver ut valmeny"""
    return


def choose():
    """returnerar användarens val."""
    return


def search_animal(zoo):
    """Menyval för vilket attribut och vad
    det ska vara för värde som det ska sökas på
     """
    return


def animal_choice():
    """Valmeny för djurattribut"""
    return

def add_animal(zoo):
    """Lägger till djur"""
    return


def sell_animal(zoo):
    """Säljer djur"""
    return


def sorter(zoo, key, reverse=False):
    """ Skriver ut djur och sorterar på parametrarna
     som är de olika djurattribut i stigande (reverse = True)
     eller fallande (reverse = False) ordning
    """
    return
def print_all(zoo):
    """Skriver ut menyval för vilka attribut
     det ska sorteras på och vilken ordning
     """
    return

def main():
    """Huvudprogrammet"""
    file = "animal_list.txt"
    zoo = Zoo(fil)
    print("Välkommen till Djurparksprogrammet.")
    print_menu()
    choice = choose()
    while choice != "A":
        choice = choose()
        zoo.save_to_file(file)
    print("Välkommen åter!")


main()
