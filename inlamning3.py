# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Joakim Bäcklund
# 2017-06-07
# scriptet har en klass tivoli med olika attraktioner man kan åka

import random


class Tivoli:
    def __init__(self,  age_min, attraktion_name, sounds, height_min=None):
        self.height_min = height_min
        if height_min is None:
            self.height_min = 0
        self.age_min = age_min
        self.attraktion_name = attraktion_name
        self.sounds = sounds

    @staticmethod
    def malfunction():
        """generar haveri 1/10, statiskmetod eftersom inget self"""
        if random.randint(0, 10) < 1:
            print('Attraktionen är tillfälligt stängd för reparation.\n')
            main_runner()
        else:
            pass

    def control(self):
        """Kollar längd och ålder"""
        height = int(input('Hur lång är du? '))
        age = int(input('Hur gammal är du? '))
        if self.height_min > height :
            print('Du är för kort för att åka denna attrakion, du är bara ' + str(height) + 'cm. \n Det krävs '
                  'minimum', self.height_min, 'längd för denna attraktion. \n Vänligen testa någon annan attraktion')
        elif self.age_min > age :
            print('Du är för ung för att åka denna attrakion, du är bara ' + str(age) + 'år.\n Det krävs '
                  'minimum', self.age_min, 'år för denna attraktion.\n Vänligen testa någon annan attraktion.')
        else:
            print('\n', self.sounds)

    def start(self):
        self.malfunction()
        self.control()

#   Funktion som frågar vilken attraktion man vill åka, while loop som gör att valet återkommer efter varje
#   Attraktionsförsök
def main_runner():
    print("Hej och välkommen till nöjesfältet Tivoli.")
    while True:
        val = int(input('\n Vad vill du åka? 1: Berg och dalbana, 2: radiobilar, 3: lustiga huset, 4: Jag vill gå hem \n'))
        if val == 1:
            Tivoli(age_min=9, height_min=150, attraktion_name="Berg och dalbana", sounds="Iiiih!").start()
        elif val == 2:
            Tivoli(age_min=9, height_min=120, attraktion_name="radiobilar", sounds="Wruum wruum!").start()
        elif val == 3:
            Tivoli(age_min=7, attraktion_name="lustiga huset", sounds="Hahaha!").start()
        elif val == 4:
            print("Välkommen åter!")
            return
        else:
            print("Vänligen gör ett val mellan 1-4")
            main_runner()



main_runner()

