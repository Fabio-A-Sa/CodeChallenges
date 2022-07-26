def getIds(passport):

    allIds = []
    for item in passport:
        allIds.append(item.split(':')[0])

    return allIds

def isValid (passport):

    answer = True
    mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for id in mandatory:
        if id not in getIds(passport):
            return False

    return True

def resolution():

    directory = "Advent of Code 2020\\Files\\Seven.txt"
    content = []
    current_passport = []

    # Get data

    with open (directory, 'r') as file:

        for line in file:

            if line != '\n':
                current_passport.append(line[0:len(line)-1])

            else:
                content.append(current_passport)
                current_passport = []

        content.append(current_passport)

    file.close()

    passports = []

    # Normalize data --> Get

    for person in content:

        passport = []
        for line in person:
            for item in line.split(' '):
                passport.append(item)
        passports.append(passport)

    counter = 0
    for passport in passports:
        if isValid(passport):
            counter += 1

    print("There are {} valid passports!".format(counter))

    return None

resolution()

# There are 247 valid passports!