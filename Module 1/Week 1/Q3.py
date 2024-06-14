import random
import math

def calculate_losses(num_samples, loss_name):
    total_loss = 0
    for i in range(num_samples):
        sample_name = f"sample {i}"
        predict = random.uniform(0, 10)  # Dự đoán ngẫu nhiên
        target = random.uniform(0, 10)   # Giá trị thực tế ngẫu nhiên
        if loss_name == 'MAE':
            loss = abs(predict - target)
            total_loss += loss
        elif loss_name == 'MSE':
            loss = (predict - target) ** 2
            total_loss += loss
        elif loss_name == 'RMSE':
            loss = math.sqrt((predict - target) ** 2)
            total_loss += loss
        else:
            raise ValueError("Invalid loss name")
        print(f"loss name: {loss_name}, sample: {sample_name}, predict: {predict:.2f}, target: {target:.2f}, loss: {loss:.2f}")
    total_loss = total_loss / num_samples
    print(f"Total {loss_name} is: {total_loss:.2f}")

def main():
    # Enter number of Sample
    num_samples = input("Enter Number of Sample: ")

    # Validate input of num_samples
    if not num_samples.isnumeric():
        print("Sample Need to be an integer!!!")
    else:
        num_samples = int(num_samples)

        # Input loss function name
        loss_name = input("Enter loss function (MAE, MSE, hoặc RMSE): ").upper()

        # Calculate loss function
        calculate_losses(num_samples, loss_name)

main()