def repeatedString(s, n):
    if (len(s) == 1):
        if (s == 'a'):
            return n
        else:
            return 0
    elif (len(s) > 1):
        count = 0
        mul = int(n / len(s))
        for x in range(len(s)):
            if s[x] == 'a':
                count = count + 1
        count = count * mul
        l = n % len(s)
        for x in range(l):
            if s[x] == 'a':
                count = count + 1
        return count

s = input()
n = int(input())
c = repeatedString(s, n)
print(c)
