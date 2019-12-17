def minimumSwaps(a):
    swaps = 0
    swaped = False
    temp = 0
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if a[j] == j+1:
                #print(a[j])
                #print("correct position")
                #print(a[j])
                continue
            else:
                a = swap(j,a)
                swaps += 1
                swaped = True
        if swaped:
            swaped = False
        else:
            break
    return swaps

def swap(j,a):
    temp = a[j]
    a[j] = a[a[j]-1]
    a[temp-1] = temp
    return a

n = int(input())
a = list(map(int, input().rstrip().split()))
r = minimumSwaps(a)
print(r)