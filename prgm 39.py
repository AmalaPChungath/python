def even_num(l):
    for i in l:
        if(i==237):
            break
        elif(not i%2):
            print(i)
n=input('Enter a collection of integers: ')
n=list(map(int,n.split()))
even_num(n)
