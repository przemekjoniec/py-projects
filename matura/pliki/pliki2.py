plik = open('plik.txt', 'r')
zawartosc = plik.readlines()
plik.close()
plik = open('plik.txt', 'w')
zawartosc = [linia.replace('A', '') for linia in zawartosc]
plik.writelines(zawartosc)
