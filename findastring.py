def find1(string, s):
    m=0
    for i in range(len(string)):
        if string[i]==s[0]:
            k=i
            j=0
            if k!=len(string)-1 & ((len(string)-k)>=len(s)):
                c = True
                while c:
                    if string[k]==s[j]:
                        j+=1
                        k+=1
                        if j==len(s):
                            m+=1
                            c=False
                    else:
                        break
    return m


string = input().strip()
sub_string = input().strip()
count=find1(string,sub_string)
print(count)