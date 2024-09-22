def displayShoppingList(shoppingList):
    print("Twoja lista:")
    for item in shoppingList:
        print("-",item)

shoppingList = []

while True:
    product = input("Wpisz produkt, lub koniec:")
    if product == 'koniec':
        break
    else:
        shoppingList.append(product)

displayShoppingList(shoppingList)