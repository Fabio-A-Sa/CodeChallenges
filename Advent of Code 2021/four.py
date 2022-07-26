def resolution():

    pairs = []
    directory = "input4.txt"
    with open(directory, 'r') as myFile:
        for line in myFile:
            pair = line.split(' ')
            pairs.append(list((str(pair[0]), int(pair[1]))))

    myFile.close()

    x, y, aim = 0, 0, 0
    for pair in pairs: 
        if pair[0] == "forward": 
            x += pair[1]
            y += pair[1]*aim
        if pair[0] == "up": aim -= pair[1]
        if pair[0] == "down": aim += pair[1]
    
    print(x, y, aim)
    return x * y

print(resolution())