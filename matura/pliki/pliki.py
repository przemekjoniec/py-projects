plik = open('plik.txt', 'w')

x = 1

while x < 101:
    plik.write(f'{x}A\n')
    x += 1

plik.close()