# x = 1
# for x in range (6):
#     print("O" * x)
#     x += 1

# O
# OO
# OOO
# OOOO
# OOOOO


# width = int(input("Podaj szerokosc trójkata: "))
# height = int(input("Podaj wysokosc trójkata: "))

# for i in range(height):
#     if i == 0 or i == height - 1:
#         print("X" * width)
#     else:
#         print("X" + " " * (width - 2)+"X")

# XXXXXXX
# X     X
# X     X
# XXXXXXX

# height = int(input("Podaj wysokosc figury: "))
# half = int(height/2)
# for i in range(height):
#     if i == 0:
#         print(" "*(height+1)+"A")
#     if i == 1 or i < height and i != half:
#         print(" "*(height-i)+"A"+" "*(((i + 1)*2)-1)+"A")
#     if i == half:
#         print(" "*(height-i)+"A"+"A"*(((i + 1)*2)-1)+"A")
        
#        A
#       A A
#      A   A
#     A     A
#    AAAAAAAAA
#   A         A
#  A           A