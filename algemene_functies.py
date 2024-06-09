argument = 4

def mijn_functie_1():
    return argument ** 2

print(mijn_functie_1())


a = 10
","
b = 5

def mijn_functie_2():
    global a
    global b
    result1 = a + b
    result2 = a - b
    result3 = a * b    
    result4 = a / b

    return [result1, result2, result3, result4]

print(mijn_functie_2())

def mijn_functie2(argument):
    mapping = {
        12.3: [15, 9, 36, 4],
        12.2: [14, 10, 24, 6],
        10.5: [15, 5, 50, 2],
        100.20: [120, 80, 2000, 5]
    }
    if argument in mapping:
        return mapping[argument]
    else: 
        return None
    
argument = 10.5

print(mijn_functie2(argument))