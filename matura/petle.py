# x = 1
# for x in range (6):
#     print("O" * x)
#     x += 1

# O
# OO
# OOO
# OOOO
# OOOOO


# width = int(input("Podaj szerokosc: "))
# height = int(input("Podaj wysokosc: "))

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


# width = int(input("Podaj szerokosc: "))
# height = int(input("Podaj wysokosc: "))
# thickness = int(input("Podaj grubosc: "))

# for i in range (height+1):
#     if i < int(height-thickness):
#         print("L"*thickness)
#     if i > int(height-thickness):
#         print("L"*width)

# LLL
# LLL
# LLL
# LLL
# LLL
# LLL
# LLLLLLLL
# LLLLLLLL


# height = int(input("Podaj wysokosc: "))

# for i in range(height):
#     if i == 0:
#         print(" "*height+"X")
#     if i > 0:
#         print(" "*(height-i)+"X"*((i*2)+1))
#      X
#     XXX
#    XXXXX
#   XXXXXXX
#  XXXXXXXXX
# 


# height = int(input("Podaj wysokosc: "))

# for i in range(height-1):
#     if i == 0:
#         print(" "*(height+1)+"X")
#     if i < height-2:
#         print(" "*(height-i)+"X"+" "*((i*2)+1)+"X")
#     else:
#         print(" "*(height-i)+"X" * (2 * height - 1))      

#       X
#      X X
#     X   X
#    X     X
#   XXXXXXXXX