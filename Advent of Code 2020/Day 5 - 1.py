def getCol (instructions):

    numbers = [int(x) for x in range (0, 8, 1)]
    for letter in instructions:
        
        if letter == 'R':
            numbers = numbers[len(numbers) // 2:]
        else:
            numbers = numbers[:len(numbers) // 2]

    return numbers[0]

def getLine (instructions):

    numbers = [int(x) for x in range (0, 128, 1)]
    for letter in instructions:
        
        if letter == 'B':
            numbers = numbers[len(numbers) // 2:]
        else:
            numbers = numbers[:len(numbers) // 2]

    return numbers[0]

def resolution():

    directory = "Advent of Code 2020\\Files\\Nine.txt"
    content = []

    with open (directory, 'r') as file:
        for line in file:
            content.append(line[:len(line)-1])
    file.close()
    
    solutions = []

    for attemp in content:

        instructionLine = attemp[:7]
        instructionCol = attemp[7:]
        line = getLine(instructionLine)
        col = getCol(instructionCol)

        id = line * 8 + col

        solutions.append(id)

    answer = max(solutions)
    print ("Max id is {}".format(answer))

    return None

resolution()

# Max id is 998