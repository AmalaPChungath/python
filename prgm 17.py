s=input('Enter a string: ')
l=[]
for i in s:
    if(i not in l):
        l.append(i)
print('removing duplicates\n',l)   
