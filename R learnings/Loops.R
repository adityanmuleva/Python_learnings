#Basic inbuilt opearations
print(seq(1,20))
print(mean(10:40))
print(sum(1:10))

#*************************************************************

# Making a function
new.function <- function() {
  for (i in 1:5) {
    print(i)
  }
}

#calling a function
new.function()

#****************************************************************

#making a function with arguments
new.function <- function(a,b,c){
  print("Hello")
  result <- a*b+c
  print(result)
}


#calling
new.function(2,3,4)


#********************************************************
