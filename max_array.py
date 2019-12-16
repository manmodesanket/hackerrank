#copied code @umyarovrr
def maxSubsetSum(a, i):
    incl = max(arr[0], arr[1], 0)

    excl = max(arr[0], 0)

    for i in range(2, len(arr)):
        incl, excl = max(incl, excl + arr[i]), incl

    return incl



n = int(input())
arr = list(map(int, input().rstrip().split()))
res = maxSubsetSum(arr, 0)
print(res)
