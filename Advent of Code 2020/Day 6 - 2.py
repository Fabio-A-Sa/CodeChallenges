from string import ascii_lowercase as abc

def normalize (something):

    alist = []
    for item in something:
        blist = []
        for word in item:
            new = ''
            for letter in word:
                if letter not in new:
                    new += letter
            blist.append(new)
            new = ''
        alist.append(blist)
        blist = []

    return alist

def resolution():
    
    directory = "Advent of Code 2020\\Files\\Six.txt"
    content = []
    current_group = []

    with open (directory, 'r') as file:
        for line in file:

            if line == '\n':
                content.append(current_group)
                current_group = []
            else:
                current_group.append(line[:len(line)-1])

        content.append(current_group)

    content = normalize(content)

    total = 0

    for group in content:
        for letter in abc:
            isValid = True
            for word in group:
                isValid = isValid and letter in word
        
            if isValid:
                total += 1
        
    print("Total is {}".format(total))
    return None

resolution()

# Total is 3360