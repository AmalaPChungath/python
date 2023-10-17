str=input('Enter a word:')
if(str.lower().endswith('ing')):
    str=str+'ly'
else:
    str+='ing'
print(str)
