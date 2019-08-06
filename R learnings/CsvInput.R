data <- read.csv("CsvInput.csv")
print(data)
print(ncol(data))
print(nrow(data))


# Get data of person having max salary
salary <- max(data$salary)
person <- subset(data, salary == max(salary))
print(salary)
print(person)

# getting details of person who works in IT department
ITDept <- subset(data, dept == "IT")
print(ITDept)
print("#########################################################################################")

# Get the persons in IT department whose salary is greater than 600
info <- subset(data, salary > 600 & dept == "IT")
print(info)

print("#########################################################################################")

# Get the people who joined on or after 2014
datadata <- subset(data, as.Date(start_date) > as.Date("2014-01-01"))
print(datadata)

