s=input('Enter a string: ')
res=''
if(len(s)<2):
    print(res)
elif(len(s)==2):
    res=s*2
    print(res)
else:
    res=s[:2]+s[-2:]
    print(res)
