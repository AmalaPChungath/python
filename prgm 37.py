n=int(input('Enter a number: '))
if(not n%2):
    print('Even')
else:
    print('Odd')
l=['1','2','3','4','5']
print(l)
item=input('Enter item to be searched: ')
if(item in l):
    print('Available')
else:
    print('Not available')
