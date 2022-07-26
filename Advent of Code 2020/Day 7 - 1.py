def resolution():

    directory = "Advent of Code 2020\\Files\\Seven.txt"
    content = []

    with open (directory, 'r') as file:
        for line in file:
            content.append(line[:len(line)-1])
    file.close()

    # ??

    total = 0
    print("Total is {}".format(total))

    return None

resolution()