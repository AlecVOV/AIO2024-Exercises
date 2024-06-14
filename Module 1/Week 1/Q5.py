import math

def calculate_MD_nRE(y, y_hat, n, p):
    MD_nRE = (y**(1/n) - y_hat**(1/n))**p
    return print(f"Result: {MD_nRE}")

calculate_MD_nRE(100, 99.5, 2, 1)
    