emp.data <- data.frame(
  emp_number = c(1:5),
  emp_names = c("aaditya", "arpita", "krishna", "jay","gaurav"),
  emp_salary = c(20,40,50,60,70),
  start_date = as.Date(c("1998-07-24","1999-07-19","2005-08-14","2001-09-25","2003-10-02"))

)


print(emp.data)
print(str(emp.data))        #To find data structure 
print(summary(emp.data))    #To find summary of data

#To get particular data from data frame
result <- data.frame(emp.data$emp_names, emp.data$emp_salary)
print(result)

#To expand data frame
emp.data$Department <- c("IT", "Operation", "HR", "IT", "Finance")
print(emp.data)


#####################################################################################################


#To add new rows in data frame we need to create one more data frame and bind them
frame_1 <- data.frame(
  name = c("Harish muleva","Kavita muleva"),
  Job = c("Head architect", "House wife")
  
)

frame_2 <- data.frame(
  name = c("santosh muleva", "anita muleva"),
  Job = c("Farmer", "House Wife")
)

resultframe <- rbind(frame_1, frame_2)
print(resultframe)











