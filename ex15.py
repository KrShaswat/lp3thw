# importing library argv from sys package
from sys import argv
# here script is for the script name and filename is to get text file
script, filename = argv
# open function opens a file in read text mode which is set to default
# open fucntion doesn't return file it makes file object.
txt = open (filename)
# it prints a message
print(f"Here's your file {filename}: ")
# this prints a file opened 
# here we run a function read() on the text file opened
# '.' here tells python to run a method (Associated with the txt function open) 
# here .read() method tells read function to run command without any parameters    
print(txt.read())

print("Type the filename again:")
file_again = input ("> ")

txt_again = open(file_again)

print(txt_again.read())
# if we open something we should close it too its good manners
txt.close()
txt_again.close()