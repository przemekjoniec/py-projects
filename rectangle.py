# def calculateArea(length, width):
#     return length*width

# length = float(input("Długość:"))
# width = float(input("Szerokość:"))

# area = calculateArea(length,width)
# print(area)
   


def findLargest(num1,num2):
    if(num1 > num2):
        print("Num1 jest wieksze",num1)
        return num1
    elif (num2 > num1):
        print("Num2 jest wieksze",num2)
        return num2
    else:
        print("Obie liczby sa równe",num2)
        return num2

v1 = findLargest(7,7)
print(v1)