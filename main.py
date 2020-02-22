""""
Fractions Calculator (To be translated to C++) by Andrew Li
"""
from Fractions import Fraction

def main():
    # main function

    # print instrustion and get input
    print("Fraction Calculator 1.0. Input a int, decimal, or fraction and the operator")
    first_input = input("First Fraction: ")
    operator = input("Operator (+, - , *, /, or **): ")
    second_input = input("Second Fraction: ")

    # unpack the strings
    input1, operator, input2 = strip_mult(first_input, operator, second_input)
    message, first_input, second_input = parse(input1, input2)

    # if parsing did not worked, print error and break
    if not message:
        print(f"The #{message} fraction or float failed to be parsed")
        return 0
    elif message == "zero d":
        print("The denomincator of the fraction cannot be 0")
        return 0

    # switch statement to check operator
    try:
        if operator == "+":
            print(f"{input1} + {input2} = {first_input + second_input}")
        elif operator == "-":
            print(f"{input1} - {input2} = {first_input - second_input}")
        elif operator == "*" or operator == "x":
            print(f"{input1} * ({input2}) = {first_input * second_input}")
        elif operator == "/":
            print(f"{input1} / ({input2}) = {first_input / second_input}")
        elif operator == "**":
            print(f"{input1} ^ ({input2}) = {first_input ** second_input}")
    except:
        print("Your input was not recognized, please try again")

    return 0


# system calls main
if __name__ == "__main__":
    main()
