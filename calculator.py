num = 0
opearation = None
reset = True
result = None
calcOperations = ["+","-","*","/","**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbe startową: "))
        reset == False
    opearation=input("Podaj operacje(" + str(calcOperations) + "),(lub exit aby wyjsc, lub reset): ")
    if opearation == "exit": break
    if opearation == "reset":
        reset = True
        continue
    if not opearation in calcOperations:
        print("Podaj poprawna operacje!")
        continue
    secondNum = int(input("Podaj druga liczbe: "))

    if opearation == "+":
        result = num + secondNum
    if opearation == "-":
        result = num - secondNum
    if opearation == "*":
        result = num * secondNum
    if opearation == "/":
        result = num / secondNum
    if opearation == "**":
        result = num ** secondNum

    print("Wynik operacji: " + str(num) + "" + opearation + "" + str(secondNum) + "=" + str(result))
    num = result
    result = None