def resolution():
    
    directory = "Advent of Code 2020\\Files\\Six.txt"
    content = []
    current_group = ''

    with open (directory, 'r') as file:
        for line in file:

            if line == '\n':
                content.append(current_group)
                current_group = ''
            else:
                current_group += line[:len(line)-1]

        content.append(current_group)

    total = 0
    for line in content:

        without_duplicates = ''
        for letter in line:
            if letter not in without_duplicates:
                without_duplicates += letter

        total += len(without_duplicates)

    print("Total is {}".format(total))
    return None

resolution()

# Total is 6625