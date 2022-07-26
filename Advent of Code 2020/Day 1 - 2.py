def resolution():

    numbers = []
    directory = "Advent\\Files\\One.txt"
    with open(directory, 'r') as myFile:
        for line in myFile:
            numbers.append(int(line))

    myFile.close()

    for X in numbers:
        for Y in numbers:
            for Z in numbers:
                if X+Y+Z == 2020:
                    print("Numbers {} and {} and {} are correct!".format(X, Y, Z))
                    print("Key = X * Y * Z = {}".format(X*Y*Z))
                    return (X, Y)
                else:
                    print("{} and {} and {}".format(X, Y, Z))
    
    return None

resolution()

# Numbers 1242 and 112 and 666 are correct!
# Key = X * Y * Z = 92643264