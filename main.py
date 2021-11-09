# Fibonacci Numbers

# Step 1 : For "Looping"
# Based on number
# The first value
f0, f1 = 0, 1
n = int(input("Enter Number : "))

# Process
for i in range(n):
    sum = f0
    f0, f1 = f1, f0 + f1
    # Result
    print(sum, end=" ")
