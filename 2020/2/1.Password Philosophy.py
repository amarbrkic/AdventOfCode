def extract(line):
    arguments = line.split()
    numberMin = arguments[0].split("-")[0]
    numberMax = arguments[0].split("-")[1]
    char = arguments[1][0]
    password = arguments[2]
    if(checkPassword(numberMin, numberMax, char, password)):
        return True


def checkPassword(numberMin, numberMax, char, password):
    br = 0
    for letter in password:
        if letter == char:
            br += 1
    if br >= int(numberMin) and br <= int(numberMax):
        return True


with open("input.txt", "r") as f:
    valid = 0
    for line in f.readlines():
        if(extract(line)):
            valid += 1
    print(valid)
