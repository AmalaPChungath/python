def whole_sum(n):
    sum=0
    if not n:return 0
    else:return n+whole_sum(n-1)
x=int(input('Enter a natural number: '))
print('The sum of %d natural numbers = %d'%(x,whole_sum(x-1)))
