line=input('Enter a line of sentence: ')
line=line.split()
words={}
for w in line:
    words[w]=words.get(w,0)+1
print(words)
