def resolution():

    directory = "Advent of Code 2020\\Files\\Five.txt"
    counter = 0
    lines = []
    content = []

    with open (directory, 'r') as file:

        for line in file:
            content.append(line[0:len(line)-1])

    file.close()

    # numberLines = len(content) --> 323
    # numberCols = len(content[0]) --> 31
    # loops = ( (numberLines * 3 ) // numberCols ) + 1 = 33

    loops = 33
    for line in content:
        step = 0
        new_line = ''
        while step != loops:
            new_line += line
            step += 1
        lines.append(new_line)
        print(new_line)

    x = 0
    for y in range(0, len(content), 1):

        attemp = lines[y][x]
        print ("{}:{} --> {}".format(y, x, attemp))

        if attemp == '#':
            counter += 1

        x = x + 3

    print ("There are {} trees in this direction".format(counter))
    return None

resolution()

# There are 164 trees in this direction