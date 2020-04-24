print("CURS 1 - TEMA - Variabile si structuri conditionale\n")

# PENTRU A TRECE LA URMATORUL PUNCT DOAR
# INTRODUCETI next :)

# 1
print("EX 1 - SIR DE NUMERE SAU DE CARACTERE? \n")

nume = input("Numele tau este: ")
while True:
    text = input("Textul pe care vrei sa il verifici este: ")
    if text == "next":
        print("\n")
        break
    elif text.isdigit():
        print("Sirul de numere a fost gasit de " + nume + "\n")
    else:
        print("Sirul de caractere a fost gasit de " + nume + "\n")

# 2
print("EX 2 - NUMAR PAR SAU IMPAR? \n")

while True:
    nr = input("Introduceti un numar: ")
    if nr == "next":
        print("\n")
        break
    elif not nr.isdigit():
        print("Mai incearca\n")
    elif int(nr) % 2 == 0:
        print("Nr e par\n")
    else:
        print("Nr e impar\n")

# 3
print("EX 3 - AN BISECT SAU NU? \n")

while True:
    an = input("Introduceti un an: ")
    if an == "next":
        print("\n")
        break
    elif not an.isdigit() or len(an) != 4:
         print("Mai incearca\n")
         continue
    elif int(an)%4 == 0:
         print("Anul e bisect\n")
    else:
         print("Anul nu e bisect\n")

# 4
print("EX 4 - NUMAR <10 SAU NEGATIV? \n")

while True:
    nr = input("Introduceti un numar: ")
    if nr == "next":
        print("\n")
        break
    elif nr.isdigit() and int(nr) < 10 and int(nr) != 0:
        print("Numarul este mai mic decat 10\n")
    elif nr[0] == "-" and nr[1:].isdigit():
        print(nr[1:] + "\n")
    elif nr.isdigit() and int(nr) == 0:
        print("Numarul este 0\n")
    elif nr.count(".") == 1 and nr[0] != "." and nr[len(nr)-1] != ".":
        a = nr.split(".")
        if a[0].isdigit() and a[1].isdigit() and float(a[0]) < 10 and float(a[1]) != 0:
            print("Numarul este mai mic decat 10\n")
        elif a[0].isdigit() and a[1].isdigit() and float(a[0]) == 0 and float(a[1]) == 0:
            print("Numarul este 0\n")
        elif a[0][0] == "-" and a[1].isdigit():
            print(nr[1:] + "\n")
        else:
            print("Mai incercati\n")
    else:
        print("Mai incercati\n")

# 5
print("EX 5 - MENIU \n")

while True:
    print("""1 – Afisare lista de cumparaturi 
2 – Adaugare element 
3 – Stergere element 
4 – Sterere lista de cumparaturi 
5 - Cautare in lista de cumparaturi \n"""
    )
    command = input()
    if command == "1":
        print("Afisare lista de cumparaturi\n")
    elif command == "2":
        print("Adaugare element\n")
    elif command == "3":
        print("Stergere element\n")
    elif command == "4":
        print("Sterere lista de cumparaturi\n")
    elif command == "5":
        print("Cautare in lista de cumparaturi\n")
    else:
        print("Alegerea nu exista. Reincercati\n")


