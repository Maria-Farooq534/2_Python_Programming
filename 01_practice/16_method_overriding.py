class Person:
    def introduce(self):
        print("Person")


class Student(Person):
    def introduce(self):
        print("Student")
        super().introduce()


class Researcher(Student):
    def introduce(self):
        print("Researcher")
        super().introduce()
        
        
student = Researcher()
student.introduce()

# MRO
print(Researcher.__mro__)



# practice challenge
# Model
#  ├── LinearRegression
#  ├── DecisionTree
#  └── NeuralNetwork

# Requirements:

# Model should have:
# predict()
# that prints something generic.
# Each child class should override predict() and print its own message.
# Create one object from each class.
# Call:
# linear.predict()
# tree.predict()
# neural.predict()
# Do not use super() yet.

class Model:
    def predict(self):
        print("ML Model.")

class LinearRegression(Model):
    def predict(self):
        print("Linear regression model prediction.")
        

class DecisionTree(Model):
    
    def predict(self):
        print("Classification Model.")
        super().predict()

        
class NeuralNetwork(Model):
    def predict(self):
        print("Used for Images, Audio, Videos.")
        
        
model = Model()
lin_reg = LinearRegression()
d_tree = DecisionTree()
n_network = NeuralNetwork()


# model.predict()
# lin_reg.predict()
# d_tree.predict()
# n_network.predict()



models = [model, lin_reg, d_tree, n_network]

for model in models:
    model.predict()
    

print(NeuralNetwork.__mro__)


print(isinstance(model, Model))
print(isinstance(lin_reg, LinearRegression))

print(issubclass(LinearRegression, Model)) # True
print(issubclass(DecisionTree, Model))   # True
print(issubclass(Model, DecisionTree))   # False
