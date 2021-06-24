print("Podaj swoj rok urodzenia:")
rok = int(input())
wiek = int(2021-rok)
if rok > 2021:
    print("Nieprawidlowy rok :( większy niż obecny")
else:
    print("Wiek: ", wiek)
    if wiek >= 18:
        print("Jestes pelnoletni :)")
    else:
        print("Nie jestes pelnoletni :(")


