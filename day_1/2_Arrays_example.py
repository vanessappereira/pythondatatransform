# Function to find the maximum value in a list of numbers.
groupNumbers = [2, 1, 5, 6, 4, 3, 8, 11, 9, 23]

smallNumber = min(groupNumbers)
bigNumber = max(groupNumbers)

value = sum(groupNumbers)
avg = round(value / len(groupNumbers), 3)

print("The smallest number is ", smallNumber)
print("The biggest number  is ", bigNumber)
print("The average  of the numbers is ", avg)
