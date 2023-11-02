def sum_list(n):
    sum=0
    for i in n:
        sum+=i
    return sum
n=input('Enter a comma separated list: ')
n=list(map(int,n.split(',')))
print(n)
print('sum of elements= ',sum_list(n))
#usng recurrsion
def sum_seq(s):
    if len(s)==1:
        return s[0]
    else:
        return s[0]+sum_seq(s[1:])
print('sum of elements= ',sum_seq(n))
