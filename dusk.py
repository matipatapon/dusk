import shutil 


def niceDisplay(table: str):
    longest = 1
    for row in table:
        for rec in row:
            if len(rec) > longest:
                longest = len(rec)
    for row in table:
        for rec in row:
            toAdd = longest - len(rec)
            print(rec+(" " * toAdd), end=" | ")
        print("\n"+(longest + 3)*"-"*len(table[0]))


def getInfo():
    f = open("/proc/mounts","r")
    content = f.read()
    f.close()
    table = [["Partition", "Mount point" , "used (Gib)", "free (%)"],]
    content = content.split("\n")
    for x in content:
        x = x.split(" ")
        if x[0][:4] == "/dev":
            mountPoint = x[1]
            total , used, free = shutil.disk_usage(mountPoint)
            v1 = f"{used // 2**30}/{total // 2**30}Gib"
            v2 = f"{round(free/total*100,2)}%"
            table.append((x[0],mountPoint,v1,v2))     
    niceDisplay(table)


getInfo()
