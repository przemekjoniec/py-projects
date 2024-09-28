num = int(input("Enter a number: "))

def calculateSquareArea(height):
    area = height * height
    print("Square area is: ", float(area))


calculateSquareArea(num)

decimal = float(input("Enter decimal number with dot: "))

def calculateSquareArea2(heigt):
    area2 = round((heigt * heigt), 2)
    print("Square area is: ", float(area2))


calculateSquareArea2(decimal)