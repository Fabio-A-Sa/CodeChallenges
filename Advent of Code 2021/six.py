'''

def getNumber(numbers, key, index = 0):

    if len(numbers) == 1: return numbers[0]
    else:
        solution = []
        for element in numbers:
            if element[index] == key[index]: 
                solution.append(element)

        return getNumber(solution, key, index+1)

def resolution():

    numbers = []
    directory = "input6.txt"
    with open(directory, 'r') as myFile:
        for line in myFile:
            numbers.append(line[:-1])

    gamma, epsilon = "", ""
    counter0, counter1 = 0, 0
    for i in range (0, len(numbers[0])):
        for element in numbers:
            if element[i] == '0': counter0 += 1 
            else: counter1 += 1
        
        if counter1 > counter0: 
            gamma += '1'
            epsilon += '0'
        elif counter1 < counter0:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
        
        counter0, counter1 = 0, 0

    i = getNumber(numbers, gamma)
    j = getNumber(numbers, epsilon)

    print(int(i, base = 2), int(j, base = 2))
    return int(i, base = 2) * int(j, base = 2)

print(resolution())

'''

def mostCommon(numbers, index):

    count1, count0, = 0, 0
    for number in numbers:
        if number[index] == '0': count0 += 1
        else: count1 += 1
    
    if count1 > count0: return '1'
    elif count1 < count0: return '0'
    else: return 'e'

def getNumber(numbers, key, index = 0):

    if len(numbers) == 1: return numbers[0]
    else:
        letter = mostCommon(numbers, index)

        if key == 'oxygen':
            if letter == 'e': letter = '1'
        else:
            if letter == 'e': letter = '0'
            elif letter == '1': letter = '0'
            else: letter = '1'

        solution = []
        for number in numbers:
            if number[index] == letter: solution.append(number)
        return getNumber(solution, key, index+1)

def resolution():

    numbers = []
    directory = "input6.txt"
    with open(directory, 'r') as myFile:
        for line in myFile:
            numbers.append(line[:-1])

    myFile.close()

    i = getNumber(numbers, 'oxygen')
    j = getNumber(numbers, 'co2')

    print(i, j)
    print(int(i, base = 2), int(j, base = 2))
    return int(i, base = 2) * int(j, base = 2)

print(resolution())