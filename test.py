# You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N
#
# students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#
# Input Format
#
# The first line contains the integer N
# , the number of students. The next
#
# lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
#
# Constraints
# 2<=N<=10
#0<=marks<=100
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
# Sample Input 0







n=int(input())

list=[]

for i in range(n):
    list.append([])

for i in range(n):
    str=input()
    list[i]=str.split(" ")

#print(list)
key=input()
sum=0

for i in range(n):
    if list[i][0]==key:
        for j in range(1,4):
            sum=sum+float(list[i][j])

sum/=3

print('%.2f'%sum)

