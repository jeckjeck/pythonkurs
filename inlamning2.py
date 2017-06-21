# Programmeringstek cklund
# 2017-06-06
# scriptet har en klass med metoder som läser in fyra meningar och skriver ut dem som en dikt


class Dikt:                                            # Skapar klass då vi har flera metoder som är lik varann
    def __init__(self):
        """Denna metod körs automatiskt när dikt anropas"""
        self.meningar = None                           # Sätter dessa instansvariabler till None så pycharm inte varnar
        self.mening_ett_split = None
        self.forsta = None
        self.resten = None

    def inmatning(self):
        """Skapar första metoden med parametern self, som står för att den bara ska ta in instansvariabler"""
        self.meningar = [input('Skriv mening nr %s:' % i) for i in range(1, 5)]  # användaren får inputta sina meningar
        # här, for loop för att slippa skriva flera rader, range(1,5)
        #  betyder att det kommer skrivas in 1-4 istället för %s

    def dela_upp(self):
        """denna metod splittar 1:a meningen och slår ihop dens 4 första och sista ord till en ny instans variabel."""
        self.mening_ett_split = self.meningar[0].split()
        self.forsta = ' '.join(self.mening_ett_split[:4])
        self.resten = ' '.join(self.mening_ett_split[4:])

    def skriv_ut(self):
        """skriver ut dikten på rätt sätt"""
        print(self.forsta.upper())
        print("\n")
        print(self.forsta)
        print(self.resten)
        print(self.forsta)
        print('\n' .join([self.meningar[i] for i in range(1, 4)]))  # print resterande meningar separerade med "ny rad"
        print(self.forsta)


def runner():
    d = Dikt()
    d.inmatning()
    d.dela_upp()
    d.skriv_ut()

runner()
