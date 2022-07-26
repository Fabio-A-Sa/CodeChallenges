def resolution():

    directory = "Advent\\Files\\Two.txt"
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

        print ("{},{} --> {}".format(key[min-1], key[max-1], letter))
        
        if (key[min-1] != letter and key[max-1] == letter ) or ():
            counter += 1
        else:
            continue

    print("Result: {} correct keys".format(counter))

    return None

resolution()

# Result: 727 correct keys