# answer: 1400
with open("input.txt", "r") as f:
    counter = 0
    prevLine = f.readline()
    lines = f.readlines()[0:]
    for line in lines:
        if(line >= prevLine):
            counter += 1
        prevLine = line
    print(counter)
