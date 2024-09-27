n=int(input())
l=[]
for i in range(n):
    command=input().split()
    if("insert" in command):
        l.insert(int(command[1])),(int(command[2]))
    elif("print" in command):
        print(l)
    elif("remove" in command):
        l.remove(int(input()))
    elif("append" in command):
        l.append(int(input()))
    elif("sort" in command):
        list.sort(l)
    elif("pop" in command):
        l.pop(int(input()))
    elif("reverse" in command):
        l.reverse()
