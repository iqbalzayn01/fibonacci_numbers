# Fibonacci Numbers

# Step 2 : Recurcion
# Process
def fibo(n):
    if n < 0:
        print("Incorrect, Try again")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(int(input("Enter Number : "))))
