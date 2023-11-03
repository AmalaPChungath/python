#fibonaacii number
def fibo(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
n=int(input('Enter a number: '))
print('%dth fibanocci number is %d'%(n,fibo(n)))
#using recurssion
def fibono(x):
    if(x==0):return 0
    if(x==1):return 1
    else:
        return fibono(x-1)+fibono(x-2)
print('%dth fibanocci number is %d'%(n,fibono(n)))
