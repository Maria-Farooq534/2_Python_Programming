# class Hierarchy

class Model:
    trained = False
    def __init__(self, name, trained):
        self.name = name
        self.trained = trained
        
    def __str__(self):
        return f"\nName: {self.name} \nModel Trained: {self.trained}"
        
    def describe(self):
        print("Model in ML is trained on set of data and learns patterns from the data and then make prediction.")

class Classification(Model):
    def __init__(self, name, trained, classes):
        super().__init__(name, trained)
        self.classes = classes
    
    def describe(self):
        print("Classification models use to make prediction about categories.")

class DecisionTree(Classification):
    def __init__(self, name, trained, classes, depth):
        super().__init__(name,trained, classes)
        self.depth = depth
    
    @property
    def depth(self):
        return self._depth
    
    @depth.setter
    def depth(self, value):
        if not isinstance(value, int):
            raise TypeError("Depth must be an integer.")
        
        if value < 0:
            raise ValueError("Depth must be a non-negative integer.")
        
        self._depth = value
        
    def describe(self):
        print("Decision Tree Model is used to take decision like an email is spam or not.")

class NeyralNetworks(Classification):
    def __init__(self, name, trained, classes, layers):
        super().__init__(name, trained, classes)
        self.layers = layers
        
    def describe(self):
        print("Neural Netowrks are the algorithms used to learn complex paterens from data.")

class Regression(Model):
    def __init__(self, name, trained, target):
        super().__init__(name, trained)
        self.target = target
        
    def describe(self):
        print("Regression model is used for sequenced data like house price prediction or match score prediction etc.")

class LinearRegression(Regression):
    def __init__(self, name, trained, target, features):
        super().__init__(name, trained, target)
        self.features = features
        
    def describe(self):
        print("Linear Regression is used to predict continuous data.")


tree = DecisionTree(
    "Image Classifier",
    True,
    ["Spam" , "Not Spam"],
    90
    
)


neural = NeyralNetworks(
    "CNN",
    True,
    ["Yes" , "No"],
    # 88,
    5
)

linear = LinearRegression(
    "Multiple Linear Regression",
    False,
    "Price",
    ["Size", "Age", "Price"]
)


# tree.describe()
# neural.describe()
# linear.describe()

models = [tree, neural, linear]

for model in models:
    model.describe()
    
    
# Inheritance Check

print(isinstance(tree , DecisionTree))
print(isinstance(tree, Classification))
print(isinstance(tree, Model))


print(issubclass(DecisionTree, Classification))
print(issubclass(DecisionTree , Model))
print(issubclass(DecisionTree , Regression))
print(issubclass(Model , DecisionTree))
print(isinstance(linear, Regression))
print(isinstance(linear, Classification))



# Property Validation

tree.depth = 6
# tree.depth = -6              # value error
print(tree.name)
print(tree.trained)
print(tree.classes)
print(tree.depth)

print(tree)
print(linear)
print(neural)