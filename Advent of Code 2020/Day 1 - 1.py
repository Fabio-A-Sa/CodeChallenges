def resolution():

    numbers = []
    directory = "Advent\\Files\\One.txt"
    with open(directory, 'r') as myFile:
        for line in myFile:
            numbers.append(int(line))

    myFile.close()

    for X in numbers:
        for Y in numbers:
            if X+Y == 2020:
                print("Numbers {} and {} are correct!".format(X, Y))
                print("Key = X * Y = {}".format(X*Y))
                return (X, Y)
            else:
                print("{} and {}".format(X, Y))
                continue
    
    return None

resolution()

# Numbers 889 and 1131 are correct!
# Key = X * Y = 1005459