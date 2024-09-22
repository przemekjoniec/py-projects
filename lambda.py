# names = ["Ola", "Ania", "Kasia"]

# ppl = map(lambda x: x + " Kowalska", names)
# ppl = list(ppl)
# print(ppl)

# filtered = filter(lambda x: len(x) > 12, ppl)
# print(list(filtered))




from functools import reduce

# numbersList = [12,20,54,75,345,76]

# totalSum = reduce(lambda a, b: a + b, numbersList)

# average = totalSum / len(numbersList)
# print(average)


users = [
    {'name' : 'Jan', 'age' : 15},
    {'name' : 'Antek', 'age' : 25},
    {'name' : 'Ola', 'age' : 30},
    {'name' : 'Kasia', 'age' : 22}
]

adults = filter(lambda user: user["age"] > 18, users)

doubleAges = map(lambda user: user["age"] * 2, adults)

totalAges = reduce(lambda x, y: x + y, doubleAges)

print(totalAges)