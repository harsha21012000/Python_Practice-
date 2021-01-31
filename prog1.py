#Largest of three numbers
a=int(input("Enter the input:"))
b=int(input("Enter the input:"))
c=int(input("Enter the input:"))
if(a>b & a>c):
    print("A is greater")
elif(b>a & b>c):
    print("B is greater")
elif(c>a & c>b):
    print("C is greater")

#factorial Program
d=int(input("num1:"))
num=1
for i in range(1,d+1):
    num=num*i
print(num)

#Sum of N Numbers
d=int(input("num1:"))
num=0
for i in range(1,d+1):
    num=num+i
print(num)

#program to swap two numbers using a temporary variable in Python
a=2
b=7
temp=a
a=b
b=temp
print(a,b)

#program to swap two numbers without using a temporary variable in Python

a=2
b=7
a,b=b,a
print(a,b)

#program to swap two numbers using bitwise operators.

a=2
b=5
a= a^b
b= a^b
a= a^b
print(a,b)

#find the maximum element 
lis=[]
num=int(input("How many Numbers"))
for i in range(num):
    number=int(input("The Numbers are:"))
    lis.append(number)
print("max element is",max(lis))

#Prime numbers Program
n=int(input("enter the number:"))
if n>1:
    for num in range(2,n):
        if((n%num)==0):
            print("not prime")
            break
            
    else:
            print("prime")
else:
    print("not prime1")
    