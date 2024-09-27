n=int(input())
inp=input().split()
l=[]
for i in range(n):
    l.append(int(inp[i]))
t=tuple(l)
print(hash(t)) 