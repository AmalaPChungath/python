a=input("Enter numbers seperated by commas\n")
s=list(map(int,a.split(",")))
even=[i for i in s if(i%2==0)]
print('Even numbers:',even)
