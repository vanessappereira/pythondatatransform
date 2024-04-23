#Create a calculator using While function

#Backend
def basicOperators(selected):

    while True:

        if option.lower() == "a":
            print("You selected option Adding");
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            sumResult = firstValue + secondValue;
            print(f"The result of the addition between {firstValue} and {secondValue} is: {sumResult}.");
            break;

        elif option.lower() == "b":
            print("You selected option Subtraction");
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            subResult = firstValue - secondValue;
            print(f"The result of the subtraction between {firstValue} and {secondValue} is: {subResult}.")
            break;

        elif option.lower( )== "c":
            print( "You selected option Multiplication" );
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            multiResult =  firstValue * secondValue;
            print(f"The result of the multiplication between {firstValue} and {secondValue} is: {multiResult} ")
            break;

        elif option.lower() == "d":
            print( "You selected option Division" );
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            if secondValue != 0 :
                divResult = firstValue / secondValue;
                print( f"The division between {firstValue} and {secondValue} is: {divResult}" )
            else:
                print( "Error! You can't divide by zero." )
            break;

        elif option.lower() == "e":
            print( "Terminating Program... See you next time" );
            break;

        else:
            print("Invalid selection, please try again.");
            break;

#Terminal
print("Welcome to the program!");
print("a. Addiction");
print("b. Subtraction");
print("c. Multiplication");
print("d. Division");
print("e. Terminate program");

option = input("Please select one of the above options: ");
basicOperators(option);