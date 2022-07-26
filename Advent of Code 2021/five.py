def resolution():

    numbers = []
    directory = "input5.txt"
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
        else:
            gamma += '0'
            epsilon += '1'
        
        counter0, counter1 = 0, 0

    print(int(gamma, base = 2), int(epsilon, base = 2))
    return int(gamma, base = 2) * int(epsilon, base = 2)

print(resolution())