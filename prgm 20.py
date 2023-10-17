l=input('Enter a list of numbers: ')
l=list(map(int,l.split()))
small1=min(l)
n=[]
for i in l:
    if(i>small1):
        n.append(i)
print('Second smallest number=',min(n))
