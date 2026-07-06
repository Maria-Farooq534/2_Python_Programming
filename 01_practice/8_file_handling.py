file = open("hello.txt")


file_content = file.read()
print(f"The file content is: {file_content}")
print(type(file_content))

file_content1 = file.read()
print(f"The file content is: {file_content1}")

file.close()