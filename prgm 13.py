a=input("Enter numbers seperated by commas\n")
a=list(map(int,a.split(",")))
#a
print("Part A")
positive=[item for item in a if(item>0)]
print(positive)
#b
print("part b")
sqr=[item**2 for item in a]
print(sqr)
#c
print("part c")
vowels=['a','A','e','E','i','I','o','O','u','U']
s1=input("Enter a string ")
s2=list(s1)
v1=[item for item in s2 if(item in vowels)]
print("vowels:",v1)
#d
print('part d')
not_even=[item for item in a if(item%2==1 or item<=0)]
print("Not even : ",not_even)
#f
print("part f")
year=int(input("Enter year "))
leap=[i for i in range(2023,year) if((i%400==0) or (i%100!=0) and (i%4==0))]
print("Leap years:",leap)
