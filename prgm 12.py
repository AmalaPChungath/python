s=input("Enter names seperated by commas\n")
names=list(s.split(','))
names=[item.split()for item in names]
count=0
print("first names\n")
for item in names:
    print(item[0])
    if(item[0][0]=="a" or item[0][0]=="A"):
        count=count+1
print("Names that start with A is",count)
