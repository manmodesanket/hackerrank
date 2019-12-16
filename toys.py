def maximumToys(prices, k):
    toys = 0
    for i in range(len(prices)):
        if prices[i] > k:
            break
        else:
            k -= prices[i]
            toys +=1
    return toys



nk = input().split()
n = int(nk[0])
k = int(nk[1])
prices = list(map(int, input().rstrip().split()))
prices.sort()
result = maximumToys(prices, k)
print(result)