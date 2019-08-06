getdata <- read.csv("CsvInput.csv")
writedata <- write.csv(getdata, "anotherone.csv")
print(writedata)