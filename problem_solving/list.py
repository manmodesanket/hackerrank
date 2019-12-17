# Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#
# Input Format
#
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
#
# Constraints
#
# There will always be one or more students having the second lowest grade.
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
#
# Berry
# Harry
# Explanation 0
#
# There are  students in this class whose names and grades are assembled to build the following list:
#
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

a=[]
m=int(input())
n=2
for i in range(0,m):
    a.append([])
for i in range(0,m):
    for j in range(0,n):
        a[i].append(j)
        a[i][j]=0

for i in range(m):
    for j in range(n):
        if j%2==0:
            a[i][j]=input()
        else:
            a[i][j]=float(input())

b=[]
for i in range(m):
    b.append(a[i][1])

b.sort()

for i in range(m):
    if b[i]!=b[i+1]:
        k=b[i+1]
        break
    else:
        pass
c=[]
for i in range(m):
    if a[i][1]==k:
        c.append(a[i][0])

c.sort()

for i in c:
    print(i)
