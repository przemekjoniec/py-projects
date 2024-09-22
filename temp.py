def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "\xB0C to ", fahrenheit, "\xB0F")
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32)* 5 / 9
    print(fahrenheit, "\xB0F to ", celsius, "\xB0C")
    return celsius


f = cToF(25)
c = fToC(77)