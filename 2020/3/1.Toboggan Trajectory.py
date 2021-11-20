# NOT DONE
with open("input.txt", "r") as f:
    pos = 0
    br = 0
    lines = f.readlines()
    for i in range(len(lines)-1):
        try:
            if(lines[i+1][pos+3] == "#"):
                br += 1
        except:
            if((lines[i+1]*(i/5))[pos+3] == "#"):
                br += 1
        pos += 3
    print(br)
