# lista = []
# x = 0
# for i in range(1 , 101):
#     if i % 2 == 0:
#         lista.append(i)
#     i += 1
# for i in range(1 , 101):
#     if i % 2 != 0:
#         lista.append(i)
#
# lista.sort(reverse=True)
# print(lista)

tekst = """Wdzięczność ludzi, wielkość świata –
Każdy siebie ma na względzie,
A drugiego za narzędzie,
Póki dobre – cacko, złoto;
Jak zepsute, ruszaj w błoto."""

ile_c = tekst.count('C') + tekst.count('c')
print('tyle jest c: ', ile_c)
ile_w = tekst.count('W') + tekst.count('w')
print('tyle jest w: ', ile_w)


