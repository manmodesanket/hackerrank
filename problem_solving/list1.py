# Consider a list (list = []). You can perform the following commands:
# 
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
# 
# Input Format
# 
# The first line contains an integer, , denoting the number of commands. 
# Each line  of the  subsequent lines contains one of the commands described above.
# 
# Constraints
# 
# The elements added to the list must be integers.
# Output Format
# 
# For each command of type print, print the list on a new line.

n=int(input())
list=[]
ml=[]
for i in range(n):
    s=input()
    list=s.split(" ")
    if list[0]=='insert':
        ml.insert(int(list[1]),int(list[2]))
    elif list[0]=='print':
        print(ml)
    elif list[0]=='remove':
        ml.remove(int(list[1]))
    elif  list[0]=='append':
        ml.append(int(list[1]))
    elif list[0]=='sort':
        ml.sort()
    elif list[0]=='pop':
        ml.pop()
    elif list[0]=='reverse':
        ml.reverse()
