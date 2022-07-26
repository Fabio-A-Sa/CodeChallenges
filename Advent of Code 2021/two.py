def resolution():

    numbers = []
    directory = "input2.txt"
    with open(directory, 'r') as myFile:
        for line in myFile:
            numbers.append(int(line))

    myFile.close()
    
    sums = []
    for i in range (0, len(numbers)-2):
        sums.append(numbers[i] + numbers[i+1] + numbers[i+2])

    counter = 0
    for i in range (0, len(sums)-1):
        if sums[i] < sums[i+1]: counter += 1

    return counter

print(resolution())