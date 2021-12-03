# answer: 4139586
with open("input.txt", "r") as f:
    lines = f.readlines()
    gamma = ""
    epsilon = ""
    arr = [0 for x in range(12)]
    for line in lines:
        for i in range(len(line)):
            if line[i] == '1':
                arr[i] += 1
    print(arr)
    arr2 = []
    for i in arr:
        arr2.append(len(lines)-i)
    for i in range(12):
        if arr[i] > arr2[i]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(int(gamma, 2)*int(epsilon, 2))
