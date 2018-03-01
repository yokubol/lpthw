# import argv variable from sys
from sys import argv

# assign two slots in argv variable
script, filename = argv

# let python open the file we entered in argv
txt = open(filename)

# print a sentence
print(f"Here's your file {filename}:")
# display content in the file we imported
print(txt.read())

# print a sentence
print("Type the filename again:")
# prompt user for a file name
file_again = input("> ")

# let python to open the file we just imported
txt_again = open(file_again)

# display the file's content we imported on the screen
print(txt_again.read())
