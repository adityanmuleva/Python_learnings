# Load the package required to read JSON files.
library("rjson")

# Give the input file name to the function.
result <- fromJSON(file = "D:\\MyLearnings\\mypylearning\\R learnings\\dataJSON.json")

# Print the result.
print(result)