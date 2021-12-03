# answer: 4139586
with open("input.txt", "r") as f:
    lines = f.readlines()
    oxArr = lines
    co2Arr = lines
    arr = [0 for x in range(5)]
    for line in lines:
        for i in range(len(line)):
            if line[i] == '1':
                arr[i] += 1
    print(arr)
    arr2 = []
    for i in arr:
        arr2.append(len(lines)-i)
    for i in range(5):
        if arr[i] > arr2[i]:
            missing = 0
            for j in lines:
                if len(j) != 5:
                    missing = 5-len(j)
                if j[i] == '0':
                    oxArr.pop(i-missing)
        else:
            missing = 0
            for j in lines:
                if len(j) != 5:
                    missing = 5-len(j)
                if j[i] == '1':
                    oxArr.pop(i-missing)
    print(oxArr)
