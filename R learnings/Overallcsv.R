# Writing data
data <- data.frame(
  name = c("aaditya muleva", "arpita muleva", "krishna muleva"),
  ID_number = 1:3,
  salary = c(1000, 2000, 3000),
  Start_date = c(as.Date("2020-01-01", "2023-01-01", "2028-01-01")),
  department = c("IT", "R&D","Health care")
)

newcsv <- write.csv(data, "Brandnew.csv")
print(newcsv)

# Reading data

getdata <- read.csv("Brandnew.csv")
print(getdata)