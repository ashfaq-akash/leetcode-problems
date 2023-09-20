arr=[[1,2,3],[4,5,6]]
rows=len(arr)
print(rows)
cols=len(arr[0])
print(cols)

transposed=[[None for _ in range(rows)]for _ in range(cols)]
print(transposed)

for i in range(rows):
    for j in range(cols):
        transposed[j][i]=arr[i][j]

print(transposed)
    