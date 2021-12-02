# answer: 1429
with open("input.txt", "r") as f:
    counter = 0
    prevSum = 0
    lines = f.readlines()
    for i in range(len(lines)-2):
        sum = 0
        for j in range(i, i+3):
            sum += int(lines[j])
        if(sum > prevSum):
            counter += 1
        prevSum = sum
    print(counter)
