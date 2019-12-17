# Complete the minimumBribes function below.
def NewYearChaos(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False

    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"

    for i in range(0, lastIndex):
        for j in range(0, lastIndex):
            if queue[j] > queue[j + 1]:
                temp = queue[j]
                queue[j] = queue[j + 1]
                queue[j + 1] = temp
                swaps += 1
                swaped = True

        if swaped:
            swaped = False
        else:
            break
    return swaps

t = int(input())

for t_itr in range(t):
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    r = NewYearChaos(a)

    if r == 0 :
        print("Too chaotic")
    else :
        print(r)

