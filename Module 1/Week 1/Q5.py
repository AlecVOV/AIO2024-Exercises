import math

def calculate_MD_nRE(y, y_hat, n, p):
    MD_nRE = abs((y**(1/n) - y_hat**(1/n))**p)
    return print(f"Result: {MD_nRE}")

calculate_MD_nRE(2, 1, 1, 2)
    