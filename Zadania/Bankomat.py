pin_uzytkownika = '1234'
stan_konta = 1000
kurs_euro = 4.7
proby = 3
pin_wpisany = input("Wprowadz pin:")
while pin_wpisany == pin_uzytkownika:
    print("\n=== MENU ===")
    print('1.Wyświetl stan konta')
    print('2.Wpłać środki')
    print('3.Wypłać środki')
    print('4.Wyświetl stan konta w EURO')
    print('5.Zakończ')
    opcja = int(input("Opcja nr:"))

    if opcja == 1:
        print('Stan konta', stan_konta)
    elif opcja == 2:
        kwota_wplata = int(input('Podaj kwote do wpłaty:'))
        if kwota_wplata > 0:
            print('Wpłacono', kwota_wplata,' złotych')
            stan_konta += kwota_wplata
        else:
            print('Kwota niepoprawna')
    elif opcja == 3:
        kwota_wyplata = int(input('Podaj kwote do wypłaty:'))
        if kwota_wyplata > stan_konta:
            print('Niewystarczajace środki')
        else:
            print('Wypłacono', kwota_wyplata,' złotych')
            stan_konta -= kwota_wyplata
    elif opcja == 4:
        print('Stan konta w EURO: ', stan_konta * kurs_euro)
    elif opcja == 5:
        break
    else:
        print('Taka opcja nie istnieje')

if pin_wpisany != pin_uzytkownika:
    while proby > 0:
        print('Podano zły pin podaj pin jeszcze raz, pozostało prób: ', proby)
        pin_wpisany = input("Wprowadz pin:")
        proby -= 1
        if proby == 0:
            break