import sys


data = input("type file name: ")
data = open(data,"r",encoding="utf-8")
data = data.readline()


if data[0].isdigit():
    s = eval(data)
    print(s)             
else: 
    data = data.split("(")
    bun = data[1].split(")")
    bun = bun[0]
    bun = bun.replace('"','')
    if data[0] == "prints":
        print(bun,"\n")
    elif data[0] == "print":
        print(bun)



sys.exit()