# answer: 2138382217
with open("input.txt", "r") as f:
    lines = f.readlines()
    xPos = 0
    yPos = 0
    aim = 0
    for line in lines:
        direction = line.split()[0]
        steps = int(line.split()[1])
        if direction == "forward":
            xPos += steps
            yPos += steps*aim
        elif direction == "down":
            aim += steps
        elif direction == "up":
            aim -= steps
    print(xPos*yPos)
