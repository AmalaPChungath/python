#a
a=int(input('Enter number: '))
b=int(input('Enter number: '))
large=lambda a,b:a if a>b else b
print('Largest number is ',large(a,b))
#b
n=int(input('Enter a number: '))
div_5=lambda a:not a%5
print(n,'is divisible by 5:',div_5(n))
#c
a=input('Enter a list: ').split()
l=list(filter(lambda x: len(x)>5,a))
print(l)
#d
a=input('Enter a list of numbers: ').split()
l=list(map(int,a))
l=list(map(lambda x:x+x*0.1 if x>1000 else x+x*0.05,l))
print(l)
