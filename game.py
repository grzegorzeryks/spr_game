import random

wrog = ["nożyce", "kamień", "papier"]
random_wrog = random.choice(wrog)

# global variablesgit
gra = 0
p_score = 0
c_score = 0
runda = 1

imie = input("Podaj swoje imie rzezimieszku :")
print("Przygotuj sie do walki {}! \n ".format(imie))

while gra < 1:
    print("!!!!!! RUNDA ", runda, "!!!!!")
    runda += 1
    moj_choice = str(input("Wybierz broń: nożyce / kamień / papier :"))
    print("Wybrałeś :", moj_choice)

    if moj_choice == "nożyce" and random_wrog == "nożyce":
        print("Wróg wybrał:", random_wrog, ". Remis")

    elif moj_choice == "nożyce" and random_wrog == "kamień":
        print("Wróg wybrał:", random_wrog, ". Przegrałeś!")
        c_score += 1

    elif moj_choice == "nożyce" and random_wrog == "papier":
        print("Wróg wybrał:", random_wrog, ". Zwyciestwo!")
        p_score += 1

    elif moj_choice == "kamień" and random_wrog == "nożyce":
        print("Wróg wybrał:", random_wrog, ". Zwyciestwo!")
        p_score += 1

    elif moj_choice == "kamień" and random_wrog == "kamień":
        print("Wróg wybrał:", random_wrog, ". Remis!")

    elif moj_choice == "kamień" and random_wrog == "papier":
        print("Wróg wybrał:", random_wrog, ". Przegrałeś!")
        c_score += 1

    elif moj_choice == "papier" and random_wrog == "nożyce":
        print("Wróg wybrał:", random_wrog, ". Przegrałeś!")
        c_score += 1

    elif moj_choice == "papier" and random_wrog == "kamień":
        print("Wróg wybrał:", random_wrog, ". Suta wygrana!")
        p_score += 1

    elif moj_choice == "papier" and random_wrog == "papier":
        print("Wróg wybrał:", random_wrog, ". Smutny remis!")

    else:
        print("Nie ma takiej broni jak {}! Wybierz jeszcze raz!".format(moj_choice))

# after you've  chosen we shall print your score and comp score
    print("Twój wynik: ", p_score)
    print("Wynik wroga: ", c_score)
    print("\n")

    if p_score == 3:
        gra = 1
        print(" {} zwycieża pojedynek!!! Twój wynik to {} do {}.".format(
            imie, p_score, c_score))

    elif c_score == 3:
        print("Przegrałeś {}! Wynikiem {} do {}.".format(imie, c_score, p_score))
        gra = 1
# the end
