# Complete the abbreviation function below.
def abbreviation(a, b):
    i = 0
    j = 0  
    flag = 0
<<<<<<< HEAD
    arr = [0] * len(a)
    for i in range(len(a)):
        if ord(a[i]) >= 65 and ord(a[i]) <= 90:
            arr[i] = 10
    i = 0    
    while i < len(b) and j < len(a):
        if b[i] == a[j] or b[i].lower() == a[j]:
            print(b[i])
            i += 1
            arr[j] = -1
            j += 1
            continue
        j += 1
        if j == len(a):
=======
    while i < len(b):
        if b[i] == a[j] or b[i].lower() == a[j]:
            i += 1
            j = 0
            print(b[i])
            continue
        j += 1
        if j == len(a) or i == len(b):
>>>>>>> a5c7483928760bc1b4f42258c11342689572914e
            flag = 1
            break
    if flag == 1:
        return 'NO'
    else:
<<<<<<< HEAD
        for i in range(len(arr)):
            if arr[i] == 10:
                return 'NO' 
=======
>>>>>>> a5c7483928760bc1b4f42258c11342689572914e
        return 'YES'        


    
q = int(input())

for q_itr in range(q):
    a = input()
    b = input()
    result = abbreviation(a, b)
    print(result)