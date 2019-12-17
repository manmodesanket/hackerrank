def prime(num):
    if(num == 1):
        return 1
    for i in range(2,num):
        if(num % i == 0):
            return 0
    return 1

x = int(input('Enter a number'))

y = prime(x)

print(y)
