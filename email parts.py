
def getEmailParts(email):
    monkeyIndex = email.find("@")
    dotIndex = email.rfind(".")
    user = email[0:monkeyIndex]
    domainName = email[monkeyIndex+1:dotIndex]
    domainExt = email[dotIndex+1:len(email)]
    table = {
        "userName" : user,
        "domain name" : domainName,
        "domain ext" : domainExt
    }
    print(table)

getEmailParts("alex@example.com")