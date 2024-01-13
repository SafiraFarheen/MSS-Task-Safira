File Handling
#Read data from Input file
f1 = open("C:/Users/safir/OneDrive/Desktop/MSS-Task/product_descriptions.txt", "r")
descriptions=f1.read()

#captalizing the first letter of each word
#title() is used to change the initial character in each word to Uppercase and the subsequent characters to Lowercase

formatted_descriptions = descriptions.title()

f2=open("C:/Users/safir/OneDrive/Desktop/MSS-Task/formatted_descriptions.txt","w")
f2.write(formatted_descriptions)
print(formatted_descriptions)
