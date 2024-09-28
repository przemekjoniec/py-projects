import math
import random

distance = random.randint(100, 1000)

fuelConsumption = 7
expecedtFuelConsumption = math.ceil(distance / 100) * fuelConsumption

fuelPrice = round(random.uniform(4.5, 5.5),2)

totalCost = round(expecedtFuelConsumption * fuelPrice,2)

print("Cost: ", totalCost)

if totalCost > 400:
    print("Too much")
else:
    print("OK")