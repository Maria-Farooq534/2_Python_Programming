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

# with open("./01_practice/hello.txt") as file:
#     lines = file.readlines()
    
# print(lines)
# print(len(lines))
# print(type(lines))

# with open("./01_practice/hello.txt" , "w") as file_1:
#     file_1.write("Hello! I'm writing in the file.")
    
# print(file_1)

# with open("./01_practice/new_file.txt" , "w") as file_2:
#     file_2.write("This is new text file.")
    
    
# with open("./01_practice/hello.txt", "r") as file_3:
#     file_2_content = file_3.read()
# print(file_2_content)


# with open("./01_practice/notes.txt" , "w") as file_4:
#     file_4.write("First line of Notes Files.\n")
#     file_4.write("Second line of File. \n")
    
# print(file_4)

with open("notes.txt", "w") as file:
    result = file.write("Hello")

print(result)
print(type(result))
