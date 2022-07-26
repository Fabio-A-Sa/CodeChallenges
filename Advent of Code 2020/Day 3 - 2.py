def resolution():

    directory = "Advent of Code 2020\\Files\\Three.txt"
    lines = []
    content = []

    with open (directory, 'r') as file:

        for line in file:
            content.append(line[0:len(line)-1])

    file.close()

    # numberLines = len(content) --> 323
    # numberCols = len(content[0]) --> 31
    # loops = ( (numberLines * 3 ) // numberCols ) + 1 = 33

    loops = 100
    for line in content:
        step = 0
        new_line = ''
        while step != loops:
            new_line += line
            step += 1
        lines.append(new_line)

    routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    solutions = []

    for route in routes:

        right, down = route
        counter = -1

        x = 0
        for y in range(0, len(content), down):

            attemp = lines[y][x]
            print ("{}:{} --> {}".format(y, x, attemp))

            if attemp == '#':
                counter += 1

            x = x + right

        print ("There are {} trees in this direction".format(counter))

        solutions.append(counter)

    answer = 1
    for solution in solutions:
        answer *= solution

    print ("Solution = {}".format(answer))

    return None

resolution()

# Solution = 5007658656