l=input("Enter a list of words: ")
n=int(input('Enter a number: '))
s=l.split()
for i in range(len(s)):
    if(len(s[i])>n):
       print(s[i])
       
