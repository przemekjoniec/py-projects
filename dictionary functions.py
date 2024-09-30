addresBook = {
    "Jan Kowalski" : {"city":"Gdansk","postalCode":"80-000"}
}

addresBook["Anna Nowak"] = {"city":"Warsaw","postalCode":"10-000"}

del addresBook["Jan Kowalski"]

addresBookCopy = addresBook.copy()

print(addresBook == addresBookCopy)
print(addresBookCopy is  addresBook)

for person in addresBook.values():
    if person["city"] == "Krakow":
        print("Person from Krakow exist")
    else:
        print("Person from Krakow doesnt exist")

print(addresBook.keys())
print(addresBook.values())