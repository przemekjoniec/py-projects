# def increaseSalary(money,bonus):
#     money = money + (money * 0.2)
#     return money + bonus

# salary = 5000
# newSalary = increaseSalary(salary,1000)

# print(salary)
# print(newSalary)


def calculateFinalPrice(initialPrice, discount):
    discountAmount = initialPrice * (discount / 100)
    finalPrice = initialPrice - discountAmount
    return finalPrice

initialPrice = float(input("Podaj kwote:"))
discount = float(input("Podaj rabat:"))

finalPrice = calculateFinalPrice(initialPrice, discount)
print("Cena: ", finalPrice)