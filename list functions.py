guests = ["Ola", "Kasia", "Adam", "Piotrek", "Patryk"]
print(len(guests))

guests.append("Pola")
guests.append("Ala")

del guests[3]

guests.sort()

dishes = ["Pizza","Burger","Tort"]

dishes.extend(["Sałatka","Ciasto"])
print(dishes[2])
dishes.pop()

if "Pizza" in dishes:
    print("Pizza znajduje sie na liscie")
    print(dishes)
else:
    dishes.append("Pizza")
    print(dishes)