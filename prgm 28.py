s=input('Enter a string: ').split()
s.sort(key=len,reverse=True)
print('Length of longest word:',len(s[0]))
if(len(s[0])==len(s[1])):
    print('BINGO')
