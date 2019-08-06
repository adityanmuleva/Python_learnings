## List, Arrays, Matrices, Vectors, Factors are different objects ##


# Vectors
# Use c() function which means to combine the elements into a vector.
myVector <- c("red", "Yellow", "Green" , "Blue")         # C represents combination
print(myVector)
print(class(myVector))

# Create a list
myList <- list(c("aaditya",20,1998), "IES IPS ACADEMY", "FOOTBALL")
print(myList)
print(class(myList))

# MATRICES
myMatrix <- matrix(c(1,2,3,4,5,6), nrow=2, ncol=3, byrow = TRUE)  # TRUE will print matrix in rows first in FALSE viceversa
print(myMatrix)
print(class(myMatrix))

# ARRAYS
myArray <- array(c("green", "yellow","black"), dim=c(3,3,2))
print(myArray)
print(class(myArray))

# Factors
myFactors <- c("apple", "banana", "Cherry", "Grape")
mFactor <- factor(myFactors)

print(myFactors)
print(mFactor)
print(nlevels(mFactor))
print(class(mFactor))
