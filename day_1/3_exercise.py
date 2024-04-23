# Function to find the maximum value in a list of numbers.
numbers = [2,1,5,6,4,3,8,11,9,23,44,128,25];

def  max_value(numbers):
    biggestNumber = max(numbers);
    print("The largest number is:",biggestNumber, "\n");

def min_values(numbers):
    smallestNumber =  min(numbers)
    print("The smallest number is: ",smallestNumber, "\n");

def total(numbers):
    totalResult = sum(numbers);
    print("The total  of all the numbers are : ",totalResult, "\n");
    
def  average(numbers):
    avgResult = round(sum(numbers)/len(numbers),3);
    print("The average of all the numbers are : ",avgResult, "\n");
     
#Frontend
print("Welcome to the program!");
while True:
    print("a. Minimum value of the array");
    print("b. Maximum value of the array");
    print("c. Total of all values ");
    print("d. Average of all values");
    print("e. Terminate program");

    option = input("Enter the letter of your choice: \n");
    if option.lower() == "a":
        min_values(numbers);

    elif option.lower() == "b" :
        max_value(numbers);

    elif option.lower() == "c":
        total(numbers);

    elif option.lower() == "d":
        average(numbers);

    elif option.lower() == "e":
        print("You've chosed to terminate the program.");
        break;
    else:
        print("Invalid Option! Please enter a valid option.");
        break;
