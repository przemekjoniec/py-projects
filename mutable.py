employee = {
    "name" : "Adam",
    "email" : "adam@email.com",
    "rank" : "programmer",
    "salary" : 8000
}

def promoteToManager (user):
    if user["rank"] == "manager":
        print("Pracownik jest menadżerem")
        return
    
    user["rank"] = "manager"
    user["salary"] *= 1.5

promoteToManager(employee)
print(employee)