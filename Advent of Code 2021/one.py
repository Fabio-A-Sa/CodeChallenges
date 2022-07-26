def resolution():

    numbers = []
    directory = "input2.txt"
    with open(directory, 'r') as myFile:
        for line in myFile:
            numbers.append(tuple(int(line)))

    myFile.close()

    counter = 0
    for i in range (0, len(numbers)-1):
        if numbers[i] < numbers[i+1]: counter += 1

    return counter

print(resolution())