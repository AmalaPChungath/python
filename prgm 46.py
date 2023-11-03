def sum_digits(x):
    if not(x/10):return x
    else:return(x%10)+sum_digits(x//10)
n=int(input('Enter a number: '))
print('sum of digits of %d=%d'%(n,sum_digits(n)))
