#answer: 2120749
with open("input.txt", "r") as f:
    lines = f.readlines()
    xPos = 0
    yPos = 0
    for line in lines:
        direction = line.split()[0]
        steps = int(line.split()[1])
        if direction == "forward":
            xPos += steps
        elif direction == "down":
            yPos += steps
        elif direction == "up":
            yPos -= steps
    print(xPos*yPos)
