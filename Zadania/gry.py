gry = [
    {'name': 'The Witcher 3: Wild Hunt', 'genre': 'RPG', 'rating': 9.8},
    {'name': 'Minecraft', 'genre': 'Sandbox', 'rating': 9.5},
    {'name': 'The Legend of Zelda: Breath of the Wild', 'genre': 'Action-Adventure', 'rating': 9.7},
    {'name': 'Cyberpunk 2077', 'genre': 'RPG', 'rating': 8.6},
    {'name': 'Dark Souls III', 'genre': 'Action RPG', 'rating': 9.4},
    {'name': 'Red Dead Redemption 2', 'genre': 'Action-Adventure', 'rating': 9.9},
    {'name': 'Fortnite', 'genre': 'Battle Royale', 'rating': 8.0},
    {'name': 'Among Us', 'genre': 'Social Deduction', 'rating': 8.5},
    {'name': 'Grand Theft Auto V', 'genre': 'Action-Adventure', 'rating': 9.6},
    {'name': 'Overwatch', 'genre': 'First-Person Shooter', 'rating': 9.0}
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
        print("test")
    elif opcja == "4":
        print("test")
    elif opcja == "5":
        print("test")
    elif opcja == "6":
        print("test")
    elif opcja == "7":
        print("test")
    elif opcja == "8":
        print("test")
    elif opcja == "9":
        print("test")
    elif opcja == "10":
        print("test")
    elif opcja == "11":
        print("test")
    elif opcja == "12":
        break