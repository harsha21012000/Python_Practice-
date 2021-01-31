#Array addition
m=int(input("row"))  #row input
n=int(input("Col"))  #col input()
matrix1=[[int(input()) for i in range(n)] for j in range(m)] #matrix1 input
for i in range(m):
    for j in range(n):
        print(matrix1[i][j],end=" ")       #Printing Matrix1 with normal space
    print()
matrix2 = [[int(input()) for i in range(n)] for j in range(m)]  #matrix2 input
for i in range(m):
    for j in range(n):
        print(format(matrix2[i][j],"<3"),end=" ")   #printing matrix2 with more space
    print()
result=[[0 for i in range(n)] for j in range(m)]  #inirializing matrix result
for i in range(m):
    for j in range(n):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(m):
    for j in range(n):
        print(format(result[i][j],"<3"),end=" ")  #result of both matrix
    print()

#Array Subtraction
m=int(input("row"))  #row input
n=int(input("Col"))  #col input()
matrix1=[[int(input()) for i in range(n)] for j in range(m)] #matrix1 input
for i in range(m):
    for j in range(n):
        print(format(matrix1[i][j],"<3"),end=" ")       #Printing Matrix1 with normal space
    print()
matrix2 = [[int(input()) for i in range(n)] for j in range(m)]  #matrix2 input
for i in range(m):
    for j in range(n):
        print(format(matrix2[i][j],"<3"),end=" ")   #printing matrix2 with more space
    print()
result=[[0 for i in range(n)] for j in range(m)]  #inirializing matrix result
for i in range(m):
    for j in range(n):
        result[i][j]=matrix1[i][j]-matrix2[i][j]
for i in range(m):
    for j in range(n):
        print(format(result[i][j],"<3"),end=" ")  #result of both matrix subtraction
    print()