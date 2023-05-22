P = float(input("Enter the principal amount: "))
I = float(input("Enter the annual rate of interest: "))
N = float(input("Enter the number of years: "))
T = P * (1 + I/100) ** N

print(T)