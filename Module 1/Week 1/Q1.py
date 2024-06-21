# The logic here is to implement a function to ask for user input 
# Then return 3 parameters and covert it too integer by map function (a built in function)
# After that allocate 3 parameter to a testing_input function => test the input to ensure the value is integer
# Passing 3 success parameter to a classification_model with F1 score


# Ask user to enter number
def user_input():
    TP = input("Please enter TP number: ")
    FP = input("Please enter FP number: ")
    FN = input("Please enter FN number: ")
    return TP, FP, FN

# Test input from user
def testing_input(TP, FP, FN):
    if isinstance(TP, int) and isinstance(FP, int) and isinstance(FN, int):
        if (TP > 0 and FN > 0 and FP > 0):
            return TP, FN, FP
        return print("Please input a positive number for testing")
    return print("Please input an integer number for testing")

# Calculate F1 Score
def evaluating_classification_model(TP, FP, FN):
    precision = TP/(TP + FP)
    recall = TP/(TP + FN)
    f1_score = 2 * (precision * recall) / (precision + recall)
    f1_score = round(f1_score, 2)
    print(f"F1 Score = {f1_score}")
    

# Using map function to modify to code to look cleanner
TP, FP, FN = map(int, user_input())
TP, FP, FN = testing_input(TP, FP, FN)
round(evaluating_classification_model(TP, FP, FN), 2)



