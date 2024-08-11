import sys
while True:

    data = input(">>>")
    if data == "exit":
        exit = input("exitしますか？[Y/N]")
        if exit == "Y"or exit == "y":
            break
        else:
            pass
    elif data[0].isdigit():
        s = eval(data)
        print(s)     
    else:
        data = data.split("(")
        bun = data[1].split(")")
        bun = bun[0]
        bun = bun.replace('"','')
        if data[0] == "outs":
            print(bun)
        elif data[0] == "out":
            sys.stdout.write(bun)


sys.exit()
