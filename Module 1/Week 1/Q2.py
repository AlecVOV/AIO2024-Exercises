import math

def is_number(number):
    if number.isnumeric():
        return float(number)
    return False

#Sigmoid Function:
def sigmoid_function(x):
    e = math.e
    sigmoid_result = 1 / (1 + pow(e, -x))
    sigmoid_result = 1 / (1 + math.exp(-x))
    return sigmoid_result

#ReLU Function:
def relu_function(x):
    if x <= 0:
        relu_result = 0  
    else:
        relu_result = x
    return relu_result

#ELU Function:
def elu_function(x):
    alpha = 0.01
    if x <= 0:
        elu_result = alpha * (math.exp(x) - 1)
    else:
        elu_result = x
    return elu_result


#Check user input 
def main():
    num = input("Please enter the number to calculate: ")
    if is_number(num) == False:
        return print("Please enter a number!!!")
    
    
    name_func = input("Input activation Function ( sigmoid | relu | elu ): ").strip().lower()
    if name_func == 'sigmoid':
        print(sigmoid_function(num)) 
    elif name_func == 'relu':
        print(relu_function(num))
    elif name_func == 'elu':
        print(elu_function(num))
    else:
        print(f"{name_func} is not supported!!!")


main()




