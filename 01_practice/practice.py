class Parameters:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    
class Bias(Parameters):
    def __init__(self, name, number, bias_value):
        super().__init__(name, number)
        self.bias_value = bias_value
        
class Weights(Parameters):
    def __init__(self, name, number, weight):
        super().__init__(name, number)
        self.weight = weight
        

parameter = Parameters("parameters" , '2')
bias = Bias("Bias" , 1 , 0.1)
weights = Weights("Weight" , 2 , '10')

print("Parameters")
print(parameter.name)
print(parameter.number)

print("Bias")
print(bias.name)
print(bias.number)
print(bias.bias_value)

print("Weights")
print(weights.name)
print(weights.number)
print(weights.weight)