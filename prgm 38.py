def rev(n):
    for i in n[::-1]:
        print(i,end=' ')
l=input('Enter your full name: ').split()
rev(l)
