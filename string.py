# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format
#
# A single line containing a string .
#
# Constraints
#0<=len(s)<=1000
#
# Output Format
#
# Print the modified string .
#
# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".
def swap_case(s):
    a=""
    for i in s:
        if i.islower()==True:
            a+=(i.upper())
        else :
            a+=(i.lower())
    return a

s=input()
a=swap_case(s)
print(a)