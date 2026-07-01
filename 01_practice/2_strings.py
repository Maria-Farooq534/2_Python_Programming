# name = "Maria Farooq"

# # Basic String Operations
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())

# # Access Characters

# print(name[4])
# print(name[-1])
# print(len(name))
# print(name.find("F"))


# # Part C — Slicing

# print(name[0:5])
# print(name[6:12])

# # Part D — Useful Functions
# print(name.startswith("Maria")) # checks if the name starts with this string or not. will return true or false.
# print(name.endswith("Farooq"))  # True

# print("Farooq" in name) # True
# print(name.count("a")) # 3 times a in the name
# print(name.index("a")) # the very first index where "a" appears

# # Part E — Replace
# # We can't modify a string directly, to do this we need to make a copy of the string and then we can modify.
# name2 = name.replace("Maria", "M")
# print(name2)
# print(name)

# # Part F — Split
# print(name.split())

# # Part G — Join
# words = ["Join", "Words", "By", "Space"]
# sentence = " ".join(words)
# print(sentence)

# ##########################################

# # Mini Practice 1
# # Input:
# # Enter full name:
# # Maria Farooq

# # Output:
# # Total characters: 13
# # Uppercase: MARIA FAROOQ
# # Lowercase: maria farooq
# # First Name: Maria
# # Last Name: Farooq

# full_name = input("Enter Full Name: ")

# print(f"Total characters: {len(full_name)}")
# print(f"Uppercase: {full_name.upper()}")
# print(f"Lowercase: {full_name.lower()}")
# print(f"First Name: {full_name[0:5]}")
# print(f"Last Name: {full_name[6:12]}")

# # Better Solution
# name_parts = full_name.split(" ")
# print(f"First Name: {name_parts[0]}")
# print(f"Last Name: {name_parts[1]}")

# ##########################################

# # Mini Practice 2
# # Input:
# # Enter sentence:
# # I love Artificial Intelligence
# # Output:
# # Number of words: 4

# input_str = input("Enter string 'I love Artificial Intelligence' : ")
# final_str = input_str.split()
# print(final_str)
# print(f"Number of Words: {len(final_str)}")

##########################################

# Mini Practice 3
# Input:
# Enter email:
# maria@gmail.com
# Output:
# Username: maria
# Domain: gmail.com

# user_email = input("Enter email: ")
# print(f"Username: {user_email[0:-10]}")
# print(f"Domain: {user_email[-10:]}")

# # Better Solution
# user_info = user_email.split("@")
# print(f"Username: {user_info[0]}")
# print(f"Domain: {user_info[1]}")


##########################################


# # Topic 2 Mini Project
# # Create:
# # Text Analyzer
# # Program should ask:
# # Enter a sentence:
# # Example:
# # I love learning Python and AI

# # Total characters: 29
# # Total words: 6
# # Uppercase:
# # I LOVE LEARNING PYTHON AND AI
# # Lowercase:
# # i love learning python and ai
# # Contains 'Python':
# # True
# # Contains 'AI':
# # True


text = input("Enter a sentence: 'I love learning Python and AI': ")

print(f"Total Characters: {len(text)}")
words = text.split()
print(f"Total words: {len(words)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

print(f"contains 'Python': {"Python" in text}")
print(f"contains 'AI': {'AI' in text}")

# print(f"contains 'Python': {text.find("Python")} ") # It gives index
# print(f"Contains 'AI': {text.find("AI")}")          # It gives index


##########################################

