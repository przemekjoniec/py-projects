plik = open('plik.txt', 'r')
zawartosc = plik.readlines()

x = 1
y = len(zawartosc)

plik2 = open('plik2.txt', 'w')
for el in zawartosc:
    liczba = int(el)
    wynik = liczba * x
    wynik_tekst = str(wynik) + '\n'
    plik2.write(wynik_tekst)
    x = wynik

plik2.close()
plik.close()
