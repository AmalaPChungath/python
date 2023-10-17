l=input('Enter a list of numbers: ')
l=list(map(int,l.split()))
for i in range(len(l)):
    if(l[i]==l[0]):
        print('Strongest neighbour of',l[i],'=',l[i+1])
    elif(l[i]==l[-1]):
        print('Strongest neighbour of',l[i],'=',l[i-1])
    else:
        if(l[i+1]>l[i-1] and l[i+1]>l[i]):
            print('Strongest neighbour of',l[i],'=',l[i+1])
        else:
            print('Strongest neighbour of',l[i],'=',l[i-1])
            
