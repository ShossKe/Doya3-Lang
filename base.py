import sys


data = input("type file name: ")
data = open(data,"r",encoding="utf-8")


for line in data.readlines():
    if line[0].isdigit():
        s = eval(data)
        print(s)             
    elif line[0] == "p": 
        line = line.split("(")
        bun = line[1].split(")")
        bun = bun[0]
        bun = bun.replace('"','')
        if line[0] == "prints":
            print(bun,"\n")
        elif line[0] == "print":
            print(bun)



sys.exit()
