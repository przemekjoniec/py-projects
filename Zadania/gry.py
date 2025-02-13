gry = [
    {'name': 'The Witcher 3: Wild Hunt', 'genre': 'RPG', 'rating': 9.8, 'year': 2000},
    {'name': 'Minecraft', 'genre': 'Sandbox', 'rating': 9.5, 'year': 2000},
    {'name': 'The Legend of Zelda: Breath of the Wild', 'genre': 'Action-Adventure', 'rating': 9.7, 'year': 2000},
    {'name': 'Cyberpunk 2077', 'genre': 'RPG', 'rating': 8.6, 'year': 2000},
    {'name': 'Dark Souls III', 'genre': 'Action RPG', 'rating': 9.4, 'year': 2000},
    {'name': 'Red Dead Redemption 2', 'genre': 'Action-Adventure', 'rating': 9.9, 'year': 2000},
    {'name': 'Fortnite', 'genre': 'Battle Royale', 'rating': 8.0, 'year': 2000},
    {'name': 'Among Us', 'genre': 'Social Deduction', 'rating': 8.5, 'year': 2000},
    {'name': 'Grand Theft Auto V', 'genre': 'Action-Adventure', 'rating': 9.6, 'year': 2000},
    {'name': 'Overwatch', 'genre': 'First-Person Shooter', 'rating': 9.0, 'year': 2000}
]

while True:
    print("======================")
    print("1. Wyświetl nazwy wszystkich gier")
    print("2. Wyświetl szczegółowe informacje o wszystkich grach")
    print("3. Wyświetl TOP 5 najlepiej ocenianych gierr")
    print("4. Wyświetl gry z wybranego gatunku")
    print("5. Dodaj grę do bazy")
    print("6. Edytuj istniejącą grę")
    print("7. Usuń grę z bazy")
    print("8. Oceń grę")
    print("9. Wyświetl szczegółowe informacje o wybranej grze")
    print("10. Zapisz bazę do pliku")
    print("11. Wczytaj bazę z pliku")
    print("12. Zakończ program")
    print("======================")
    opcja = input("Wybierz opcje: ")
    if opcja == "1":
        print("Nazwy gier w bazie:")
        for element in gry:
            print(element['name'])
    elif opcja == "2":
        print("Informacje o grach w bazie:")
        for element in gry:
            print("Nazwa: " + element['name'])
            print("Gatunek: " + element['genre'])
            print("Ocena: " + str(element['rating']))
    elif opcja == "3":
        gry.sort(key=lambda x: x['rating'], reverse=True)
        for element in gry[:5]:
            print(element['name'])
    elif opcja == "4":
        znaleziono = False
        gatunek = input("Podaj gatunek: ")
        for element in gry:
            if gatunek.upper() == element['genre']:
                print(element['name'])
                znaleziono = True
            if not znaleziono:
                print("Nie znaleziono")
                break
    elif opcja == "5":
        nazwa = input("Podaj nazwe: ")
        gatunek = input("Podaj gatunek: ")
        ocena = input("Podaj ocene: ")
        rok = input("Podaj rok wydania: ")
        gry.append({'name': nazwa, 'genre': gatunek, 'rating': ocena, 'year': rok})
    elif opcja == "6":
        print("nie chce mi sie")
    elif opcja == "7":
        nazwa = input("Podaj nazwe: ")
        for element in gry:
            if nazwa == element['name']:
                gry.remove(element)
    elif opcja == "8":
        nazwa = input("Podaj nazwe: ")
        ocena = int(input("Podaj ocene: "))
        for element in gry:
            if nazwa == element['name']:
                element['rating'] = ocena
    elif opcja == "9":
        nazwa = input("Podaj nazwe: ")
        for element in gry:
            if nazwa == element['name']:
                print("Nazwa: " + element['name'])
                print("Gatunek: " + element['genre'])
                print("Ocena: " + str(element['rating']))
    elif opcja == "10":
        plik = open('baza.txt', 'w')
        for element in gry:
            plik.write('Nazwa: ' + str(element['name']) + ' Gatunek: ' + str(element['genre']) + ' Ocena: ' + str(element['rating']) + ' Rok wydania: ' + str(element['year']) + '\n')
        plik.close()
    elif opcja == "11":
        break