myarray1 <- c(1,2,3)
myarray2 <- c(4,5,6,7,8,9)

row.names <- c("row1", "row2", "row3")
column.names <- c("col1", "col2", "col3")
matrix.names <- c("Matrix_1", "Matrix_2")

result <- array(c(myarray1,myarray2), dim=c(3,3,2), dimnames=list(row.names, column.names, matrix.names))

#Accessing array elements
print(result[2,2,1])
print(result[,,2])
print(result[2,,1])

print(result)

#####################################################################################################
vector1 <- c(1,2,3)
vector2 <- c(4,5,6,7,8,9)
result1 <- array(c(vector1,vector2),dim = c(3,3,2))

vector3 <- c(10,11,12)
vector4 <- c(13,14,15,16,17,18)
result2 <- array(c(vector3,vector4),dim = c(3,3,2))

matrix1 <- result1[,,2]
matrix2 <- result2[,,2]

finalresult <- matrix1+matrix2
print(finalresult)

