# VALIDATOR CNP
while True:
    CNP = input("Introduceti un CNP: ")

    # Verificari Initiale
    if not CNP.isdigit():
        print("CNP incorect! CNP ul contine si alte caractere inafara de cifre!")
        break
    elif len(CNP) > 13:
        print("CNP incorect! CNP ul contine prea multe cifre!")
        break
    elif len(CNP) < 13:
        print("CNP incorect! CNP ul contine prea putine cifre!")
        break

    S = CNP[0]
    AA = CNP[1:3]
    LL = CNP[3:5]
    ZZ = CNP[5:7]
    JJ = CNP[7:9]
    NNN = CNP[9:12]
    C = CNP[12]

    # Sex
    if int(S) in [1, 3, 5, 7]:
        print("Sex barbatesc")
    elif int(S) in [2, 4, 6, 8]:
        print("Sex femeiesc")
    elif S == "9":
        print("Persoana straina")
    elif S == "0":
        print("CNP gresit! Sexul nu poate fi 0")
        break

    # An
    if S == "1" or S == "2":
        print("Anul nasterii este 19"+AA)
    elif S == "3" or S == "4":
        print("Anul nasterii este 18"+AA)
    elif S == "5" or S == "6":
        print("Anul nasterii este 20" + AA)
    else:
        print("Anul nasterii este 19"+AA)

    # Luna
    Luna = {
             1: 'Ianuarie', 2: 'Februarie', 3: 'Martie',
             4: 'Aprilie', 5: 'Mai', 6: 'Iunie',
             7: 'Iulie', 8: 'August', 9: 'Septembrie',
             10: 'Octombrie', 11: 'Noiembrie', 12: 'Decembrie'
            }

    if LL == "00":
        print("CNP gresit. Luna nu poate fi 00")
        break
    elif LL[0] == "0":
        print("Luna nasterii este " + Luna[int(LL[1:])])
    else:
        print("Luna nasterii este " + Luna[int(LL)])

    # Ziua
    if ZZ == "00":
        print("CNP gresit! Ziua nu poate fi 00")
        break
    elif int(ZZ) > 31:
        print("CNP gresit! Nu exista o zi > 31")
        break
    else:
        print("Ziua nasterii este " + ZZ)

    # Judet
    Judete = {
                1: 'Alba', 2: 'Arad', 3: 'Arges', 4: 'Bacau', 5: 'Bihor',
                6: 'Bistrita-Nasaud', 7: 'Botosani', 8: 'Brasov', 9: 'Braila',
                10: 'Buzau', 11: 'Caras-Severin', 12: 'Cluj', 13: 'Constanta',
                14: 'Covasna', 15: 'Dambovita', 16: 'Dolj', 17: 'Galati',
                18: 'Gorj', 19: 'Harghita', 20: 'Hunedoara', 21: 'Ialomita',
                22: 'Iasi', 23: 'Ilfov', 24: 'Maramures', 25: 'Mehedinti',
                26: 'Mures', 27: 'Neamt', 28: 'Olt', 29: 'Prahova',
                30: 'Satu Mare', 31: 'Salaj', 32: 'Sibiu', 33: 'Suceava',
                34: 'Teleorman', 35: 'Timis', 36: 'Tulcea', 37: 'Vaslui',
                38: 'Valcea', 39: 'Vrancea', 40: 'Bucuresti', 41: 'Bucuresti S1',
                42: 'Bucuresti S2', 43: 'Bucuresti S3', 44: 'Bucuresti S4',
                45: 'Bucuresti S5', 46: 'Bucuresti S6', 51: 'Calarasi', 52: 'Giurgiu'
              }

    if int(JJ) > 52 or JJ == "00" or int(JJ) in [47, 48, 49, 50]:
        print("CNP gresit! Judetul nu exista")
        break
    elif JJ[0] == "0":
        print("Judetul " + Judete[int(JJ[1:])])
    else:
        print("Judetul " + Judete[int(JJ)])

    # NNN
    if NNN == "000":
        print("CNP gresit! Numarul NNN nu poate fi 000")
        break
    else:
        print("Numar " + NNN)

    # Cod autodetector
    numar = "279146358279"
    res = 0

    for i in range(0, 12):
        res += int(numar[i]) * int(CNP[i])

    cifra = res % 11

    if cifra == 10:
        cifra = 1

    if cifra == int(C):
        print("CNP corect! Cifra de control " + C)
    else:
        print("CNP incorect! Cifra de control incorecta!")
