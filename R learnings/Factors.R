data <- c("East","west","North","East","west","North","East","East","west")
print(data)
print(is.factor(data))

#factoring data
data_factor <- factor(data)
print(data_factor)
print(is.factor(data_factor))

#################################################################################
#Factors in data frame
Height <- c(123, 124,125,126,127,128,129,130)
Weight <- c(45,50,55,60,65,70,75,80)
Gender <- c("male","female", "male","female","male","female","male","male")
input_data <- data.frame(Height,Weight,Gender)
print(input_data)

print(is.factor(input_data$Gender))
print(input_data$Gender)