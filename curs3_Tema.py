import random


# find all occurrences for a letter in a string
def find_all_letters(word, let):
    pos = []
    for j in range(0, len(word)):
        if word[j] == let:
            pos.append(j)
    return pos


words = ["temperament", "schizofrenic", "alfabeticește", "sternocleidomastoidian", "electrocardiograma",
         "xilofon", "pneumatic", "zbenghi", "transplant", "coincidenta", "pupaza",
         "destrabalare", "monetarie", "latifundiar", "opiaceu", "complexitate", "spectru"]

word_to_guess = words[random.randint(0, 16)]
word_guessed = []

for i in range(0, len(word_to_guess)):
    word_guessed.append("_")

no_tries = 8
tried_letters = []

print("Cuvantul de ghicit are " + str(len(word_to_guess)) + " litere")
print(''.join(word_guessed) + '\n')

while no_tries > 0:
    print("Numar incercari ramase: " + str(no_tries))
    letter = input("Litera/Cuvantul dvs este: ")

    # Am incercat deja aceasta litera
    if tried_letters.count(letter) != 0:
        no_tries -= 1
        print(''.join(word_guessed))
        print("Litera deja incercata!\n")
        continue

    # Daca am dat ca input o litera
    if len(letter) == 1:

        tried_letters.append(letter)
        no_matches = len(find_all_letters(word_to_guess, letter))
        matches = find_all_letters(word_to_guess, letter)

        # Nu am match pe litera
        if no_matches == 0:
            no_tries -= 1
            print(''.join(word_guessed))
            print("Mai incercati!\n")

        # Am cel putin un match pe litera
        elif no_matches > 0:
            for i in range(0, no_matches):
                word_guessed[matches[i]] = letter

            if ''.join(word_guessed) == word_to_guess:
                print("Felicitari!")
                break

            print(''.join(word_guessed))
            print("Litera corecta! Continuati!\n")

    # Daca am dat ca input un cuvant
    elif letter == word_to_guess:
        print("Felicitari!")
        break

    else:
        no_tries -= 1
        print("Mai incercati!\n")

# Daca am ramas fara incercari
if no_tries == 0:
    print("Data viitoare!")
