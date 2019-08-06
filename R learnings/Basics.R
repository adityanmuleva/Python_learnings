data <- data.frame(
  name = c("aaditya", "arpita"),
  ID_NO = 1:2,
  class = c(12,12),
  hobby = c("playing football", "painting")
)
newFile <- write.csv(data, "TEST.csv")
print(newFile)

