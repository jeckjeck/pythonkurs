# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# Joakim Bäcklund
# 2017-06-06
# Beräknar antalet iterationer för ett fyrsiffrigt heltal att nå 6174 genom kaprekars formel.
# Skriver också ut felmeddelanden vid ev. fel.


def kaprekar():
    tal = input("Ange ett fyrsiffrigt heltal: ")
    i = 0
    while tal != '6174':
        if len(tal) != 4:               # Anger villkor som kollar om antalet siffror i tal är annat än 4
             tal = str(tal + "0")
        if len(list(set(tal))) <= 1:    # om siffrorna i talet innehåller bara samma siffror så ska den identerade
            # koden efter kolonet köras
            print("talet innehåller för många likadana siffror vid iteration:", i, "eftersom talet är:", tal)
            return
        large = "".join(sorted(tal, reverse=True))   # Tar fram största talet av de fyra siffrorna talet består av
        small = "".join(sorted(tal))
        tal = str(int(large) - int(small))
        i += 1
    return print("Det tog", i, "st. iterationer att nå talet 6174")


kaprekar()
