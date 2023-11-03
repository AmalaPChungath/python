def rev_str(x):
    if not len(x):
        return ''
    else:
        return x[-1]+rev_str(x[:-1])
s=input('Enter a string: ')
print('Reversed string = ',rev_str(s))
