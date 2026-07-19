# module is a python file that has python code.
print("Hello")

# def hello():
#     print("Hello and welcome!")
    
def sum(a,b):
    print(a + b)
    

numbers = [1,2,3]
    
    
# count = 0

# def hello():
#     global count
#     # count += 1
#     print(count)
    
count = 10
def hello():
    new_count = count + 5
    print(new_count)
    
# hello()
# print(count)

def increase(): # instead of chnaging count variable in each file. we can simply define a function for increment and call the function whenever we want to change or incremnt the vlaue.
    global count
    count += 1
    print(count)
    # return count