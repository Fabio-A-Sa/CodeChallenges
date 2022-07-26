def splitData(passport):

    all = []
    for item in passport:
        key, content = item.split(':')[0], item.split(':')[1]
        all.append(list([key, content]))

    return all
    
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

    directory = "Advent of Code 2020\\Files\\Four.txt"
    content = []
    current_passport = []

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
    for person in content:

        passport = []
        for line in person:
            for item in line.split(' '):
                passport.append(item)
        passports.append(passport)

    valids = []
    for passport in passports:
        if isValid(passport):
            valids.append(passport)

    answer = 0
    for passport in valids:

        v = True
        for key, content in splitData(passport):

            if key == 'byr':
                v = v and int(content) in [int(x) for x in range (1920, 2003, 1)]
            
            if key == 'iyr':
                v = v and int(content) in [int(x) for x in range (2010, 2021, 1)]

            if key == 'eyr':
                v = v and int(content) in [int(x) for x in range (2020, 2031, 1)]

            if key == 'hgt':
                
                secondKey = content[len(content)-2:]
                if secondKey in ['cm', 'in']:

                    if secondKey == 'cm':
                        number = int(content[:len(content)-2])
                        v = v and number in [int(x) for x in range (150, 194, 1)]
                    else:
                        number = int(content[:len(content)-2])
                        v = v and number in [int(x) for x in range (59, 77, 1)]

            if key == 'hcl':
                
                if content[0] == '#':
                    for letter in content[1:]:
                        v = v and letter in ['a', 'b', 'c', 'd', 'e', 'f'] + [str(x) for x in range (0, 10, 1)]
                    v = v and len(content[1:]) == 6

                else:
                    v = False

            if key == 'ecl':
                v = v and content in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

            if key == 'pid':
                
                for digit in content:
                    v = v and digit in [str(x) for x in range (0, 10, 1)]
                v = v and len(content) == 9

        if v: 
            answer += 1
        else:
            continue

    print("There are {} valid passports!".format(answer))

    return None

resolution()

# There are 145 valid passports!