rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of Columns: "))

matrix =[]

for i in range(rows):
    ele = []
    for j in range(columns):
        d=int(input(j))
        ele.append(d)
    matrix.append(ele)

print(matrix)





# for i in matrix:
#     for j in i:
#         print(matrix[i] + matrix[j])
#         break
