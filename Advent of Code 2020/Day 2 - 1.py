def resolution():

    directory = "Advent\\Files\\Three.txt"
    counter = 0
    lines = []

    with open(directory, 'r') as file:
        for line in file:
            lines.append(line)

    file.close()

    for line in lines:
        
        letter = line[line.find(':')-1]
        key = line[line.find(':')+1::]
        min = int(line[0:line.find('-')])
        max = int(line[line.find('-')+1:line.find(':')-2])

        # print ("Min: {} Max: {} Letter: {} Key: {}".format(min, max, letter, key))

        attemp = 0

        for x in key:
            if x == letter:
                attemp += 1
            else:
                continue

        if attemp in range(min, max+1):
            counter += 1
        else:
            continue

    print("Result: {} correct keys".format(counter))

    return None

resolution()

# Result: 620 correct keys