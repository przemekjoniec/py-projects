def createUserProfile(firstName, lastName, age, city):
    return {"firstName" : firstName, "lastName" : lastName, "age" : age, "city" : city}

firstName=input("Podaj imie: ")
lastName=input("Podaj nazwisko: ")
age=input("Podaj wiek: ")
city=input("Podaj miasto: ")

userProfile = createUserProfile(firstName=firstName, lastName=lastName, age=age, city=city)
print(userProfile)