# file = open("./01_practice/hello.txt")


# file_content = file.read()
# print(f"The file content is: {file_content}")
# print(type(file_content))

# file_content1 = file.read()
# print(f"The file content is: {file_content1}")

# file.close()

# when we use file.read() , python first check if the file is open or not. then condition2, checks where the pointer is?

# file_content.read()  # will give error, bcz the file is already closed.

# if the file is open but the pointer is at the end, then it returns an empty string.

# with open("./01_practice/hello.txt") as file1:
#     content = file1.read()
    
# print("new content: ")
# print(content)

# with open("./01_practice/hello.txt") as file3:
#     line1 = file3.readline()
    
    
# print(line1)

with open("./01_practice/hello.txt") as file:
    lines = file.readlines()
    
print(lines)
print(len(lines))
print(type(lines))

