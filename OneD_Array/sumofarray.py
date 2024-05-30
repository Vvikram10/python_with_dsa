print("Enter size of array")
n = int(input("size is "))

sum = 0  # Initialize sum to 0

for i in range(n):
    ele = int(input("Enter element: "))
    sum += ele  # Add the input element directly to the sum

print("sum is", sum)

