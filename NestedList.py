l1=[]
min=0.0
index=0
for i in range(int(input())):
    name=input()
    score=float(input())
    l1.append([name,score])
l1.sort(key=lambda x:x[1])
lowest=l1[0][1]
second_lowest=None
for i in l1:
    if i[1]>lowest:
        second_lowest=i[1]
        break
second_lowest_names=[i[0] for i in l1 if i[1]==second_lowest]
second_lowest_names.sort()
for name in second_lowest_names:
    print(name)