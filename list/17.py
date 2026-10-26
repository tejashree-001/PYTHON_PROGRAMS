#Create two 3 × 3 matrices using nested lists and performmatrix addition.


matrix1 =[
  [1,2,3],
  [4,5,6],
  [7,8,9]

]

matrix2=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

result=[]

for i in range(3):
    row=[]
    for j in range(3):
        row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row)


print("Matrix1")

for i in matrix1:
    print(i)

print("Matrix2")
for i in matrix2:
    print(i)

print("Addtition of two matrices:")
for i in result:
    print(i)
    