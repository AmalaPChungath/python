def count_strg(s):
    count=0
    for item in s.split():
        if(len(item)>1 and item[0]==item[-1]):
            count+=1
    return count
s=input('Enter a collection of string ')
print(count_strg(s))
