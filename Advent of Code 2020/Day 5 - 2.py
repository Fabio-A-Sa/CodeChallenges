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

    directory = "Advent of Code 2020\\Files\\Five.txt"
    content = []

    with open (directory, 'r') as file:
        for line in file:
            content.append(line[:len(line)-1])
    file.close()
    
    solutions = []

    matrix = []
    for y in range (0, 128, 1):
        current_line = []
        for x in range (0, 8, 1):
            current_line.append('O')
        matrix.append(current_line)
        current_line = []

    for attemp in content:

        instructionLine = attemp[:7]
        instructionCol = attemp[7:]
        line = getLine(instructionLine)
        col = getCol(instructionCol)

        id = line * 8 + col

        solutions.append(id)

        matrix[line][col] = 'X'

    answer = max(solutions)
    print ("Max id is {}".format(answer))

    for x in matrix:
        line = ''
        for y in x:
            line += y
        print(line)

    id = 84 * 8 + 4
    print("My id is {}".format(id))

    return None

resolution()

# Max id is 998
# My id is 676