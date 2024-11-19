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


# # height = int(input("Podaj wysokosc: "))

# # for i in range(1, height+1):
# #     for j in range(1, i+1):
# #         print (j, end=" ")
# #     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# height = int(input("Podaj wysokosc: "))

# for i in range(1, height+1):
#     x = i
#     for j in range(1, i+1):
#         print (i, end=" ")
#         i = i+x
#     print()

# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25

# height = int(input("Podaj wysokosc: "))

# for i in range(1, height+1):
#     for j in range(i):
#         print (3*(i-1+j), end=" ")
#     print()

# 0
# 3 6
# 6 9 12
# 9 12 15 18
# 12 15 18 21 24

# WYKONAC JESZCZE RAZ