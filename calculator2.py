num1 = 0
num2 = 0
operation = None
result = 0

while True:
    operation=input("Podaj operacje: add, sub, mul, div, pow, exit: ")
    num1=int(input("Podaj pierwsza cyfre: "))
    num2=int(input("Podaj druga cyfre: "))
    if operation == "add":
        result = num1 + num2
    if operation == "sub":
        result = num1 - num2
    if operation == "mul":
        result = num1 * num2
    if operation == "div":
        result = num1 / num2
    if operation == "pow":
        result = num1 ** num2
    if operation == "exit":
        break
    else:
        print("Nieznane działanie")

    print("Wynik działania na twoich liczb to:", result)
    result = 0