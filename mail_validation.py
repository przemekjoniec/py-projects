email = input("Enter email: ")

def validateEmail(email):
    monkeyIndex = int(email.find("@"))
    dotIndex = int(email.find("."))

    if dotIndex < monkeyIndex:
        print("Write correct email!")
    else:
        if monkeyIndex > -1 and dotIndex > -1:
            print("Good email!")
        else:
            print("Bad email!")

validateEmail(email)