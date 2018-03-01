from sys import argv

scriptName, firstVar, secondVar = argv

print("The script is called:", scriptName)
fruit = input("Enter your favourite fruit: ")
print("So your variables are {} and {} and your favourite fruit is {}.".format(firstVar, secondVar, fruit))
# print(f"So your variables are {} and {} and your favourite fruit is {}.") # error
print(f"So your variables are {firstVar} and {secondVar} and your favourite fruit is {fruit}.")
