s1=input('Enter a collection 1 of integers: ')
s2=input('Enter a collection 2 of integers: ')
s1=set(map(int,s1.split()))
s2=set(map(int,s2.split()))
print('list of same length:',len(s1)==len(s2))
print('The collections sum to same value:',sum(s1)==sum(s2))
print('Are there commmon elements:',bool(len(s1&s2)))
