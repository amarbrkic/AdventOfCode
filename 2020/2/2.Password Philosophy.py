def extract(line):
    arguments = line.split()
    numberMin = arguments[0].split("-")[0]
    numberMax = arguments[0].split("-")[1]
    char = arguments[1][0]
    password = arguments[2]
    if(checkPassword(numberMin, numberMax, char, password)):
        return True
    return False


def checkPassword(numberMin, numberMax, char, password):
    br = 0
    if (char == password[int(numberMin)-1] and char != password[int(numberMax)-1]) or (char != password[int(numberMin)-1] and char == password[int(numberMax)-1]):
        return True
    return False


with open("input.txt", "r") as f:
    valid = 0
    for line in f.readlines():
        if(extract(line)):
            valid += 1
    print(valid)
