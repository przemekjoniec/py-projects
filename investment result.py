capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

earnedMoney = capital * rateOfInterest
lostMoney = capital * inflationRate

newCapital = capital + earnedMoney - lostMoney
print(newCapital)