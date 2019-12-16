def rotLeft(a,d):
    temp = 0
    l = len(a)
    b = [0] * l
    for i in range(0,l):
        index = (i + d) % l
        b[i] = a[index]
    return b

nd = input().split()
n = int(nd[0])
d = int(nd[1])

a = list(map(int,(input().rstrip().split())))
a = rotLeft(a,d)
for i in range(0,len(a)):
    print(a[i],end=" ")