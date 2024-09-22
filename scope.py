# employess = []

# def addEmployee(email,salary):
#     e = {
#         "email" : email,
#         "salary" : salary
#     }
#     employess.append(e)

# addEmployee("ania@test.com",6000)
# addEmployee("ola@test.com",7500)
# addEmployee("adam@test.com",8000)

# def increaseSalary(employess, pctIncrease):
#     pctIncrease *= 0.01

#     for e in employess:
#         e["salary"] *= 1 + pctIncrease

# increaseSalary(employess, 20)
# print(employess)


accountBalance = 0

def addFunds(amount):
    global accountBalance
    accountBalance += amount
    print("Dodano środki:", amount)

def withdrawFunds(amount):
    global accountBalance
    if amount > accountBalance:
        print("Niewystarczające środki!")
    else:
        accountBalance -= amount
        print("Wypłacono środki:", amount)

def checkFunds():
    print("Twoje środki:", accountBalance)

while True:
    action = input("Wybierz: dodaj, wyplac, stan, koniec: ")
    if action == "koniec":
        break
    elif action == "dodaj":
        amount = float(input("Podaj kwote: "))
        addFunds(amount)
    elif action == "wyplac":
        amount = float(input("Podaj kwote: "))
        withdrawFunds(amount)
    elif action == "stan":
        checkFunds()
    else:
        print("Nieznane działanie!")