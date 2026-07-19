# import greetings

from greetings import count
print(count)

count = 50
print(count)

from greetings import numbers
print(numbers)
numbers.append(4)
# print(numbers)
# print(greetings.numbers)

# greetings.hello()
# greetings.hello()
# greetings.hello()




# import greetings
# greetings.hello()
# # greetings.sum(2, 4)
# print(greetings)



# count = 100
# count = greetings.count
# count = count + 5
# print(count)
# print(greetings.count)

# greetings.count += 5  this is not the good way to modify the variable. 


# print(greetings.count)
# greetings.increase()


# a = greetings
# a.count = 50
# print(a.count)
# print(greetings.count)

# print(a is greetings)

# x = 2
# y = x
# print(x)
# print(y)
# print(x is y)

a = [1,2,3]
b = a.append(3)
print(a)
print(b)

a = [1,2,3]
b = a
c = a.copy()
a.append(4)

print(a)
print(b)
print(c)

print(a is b)
print(b is a)
print(c is a)