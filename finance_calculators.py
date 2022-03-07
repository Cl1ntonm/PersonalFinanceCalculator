import math
# Capstone Project 1 - Compulsory Task - Financial calculator
# Author - Clinton M
# Program purpose, user to chooses either investment option to calculate there interest earned
# or a Bond option to calculate the amount needed to pay a home loan

# Requesting user to choose the calculator by typing either investment or Bond
print("Financial Calculator")
print(" ")
print("Choose either 'investment' or 'bond' from the menu bellow to proceed")
print(" ")
print("investment       - to calculate the amount of interest you'll earn on amount invested")
print("bond             - to calculate the amount you'll have to pay on your home loan ")
print(" ")

# assigning Base values
calculator_type = "Not yet"
interest_type = "Not yet"

# requesting user input of either investment or bond calculator while allowing the user to re-enter the correct
# option if needed
response = True
while response:
    # changing the case of input in order to accept any case variation (upper otr lower)
    calculator_type = input("").lower()

    if calculator_type == "investment":
        print(" ")
        print("You chose the investment calculator")
        print(" ")
        break
    elif calculator_type == "bond":
        print(" ")
        print('You chose the Bond calculator')
        print(" ")
        break
    else:
        print(" ")
        print("You have entered an incorrect option , Please try again ")
        print("Please enter either  'investment' or 'bond'")
        print(" ")

# calculating the interest of the investment

# assigning a base value
total_with_interest = 0

# depending on calculator chosen ( investment or bond) conditional statement used to apply the appropriate equation
if calculator_type == "investment":
    # request user input , all the values needed to perform the calculation
    deposit_amount = float(input("Please enter the amount to be deposited into the account: "))
    interest_rate = float(input("please Enter the interest rate: "))
    number_years = int(input("Please enter the number of years you would like to invest for: "))

    # re-assigning the variable to simplify equation readability
    A = total_with_interest
    P = deposit_amount
    r = interest_rate / 100
    t = number_years

    # requesting the user to choose between a simple or compound interest calculation
    # and utilising a loop structure to allow for the correct input if needed
    interest_response = True
    while interest_response:
        # changing the case of input in order to accept and case variation (upper otr lower)
        interest_type = input("Which type of interest calculation would you like ? 'simple' or 'compound' ").lower()

        # requesting user input of either simple or compound interest type while allowing the user to
        # re-enter the correct option if needed
        if interest_type == "simple":
            print(" ")
            print(f"You chose the {interest_type} interest type")
            break
        elif interest_type == "compound":
            print(" ")
            print(f"You chose the {interest_type} interest type")
            break
        else:
            print("You have entered the incorrect input , Please try again ")
            interest_type = input("Which type of interest calculation would you like ? 'simple' or 'compound' ").lower()

    # Calculate the ,simple interest calculation,A = P(1 + r * t)
    if interest_type == "simple":
        # simple interest calculation with python appropriate syntax
        A = P * (1 + r * t)

        # Calculate the, compound interest calculation , A = P(1 + r) ^ t
    elif interest_type == "compound":
        # compound interest calculation with python appropriate syntax
        A = P * math.pow((1 + r), t)
    A = round(A,2)
    print(" ")
    print(f"The Total earned with interest is {A}")

# Calculation the Bond repayment
if calculator_type == "bond":
    # Requesting the user to input the information needed to calculate
    print(" ")
    property_value = float(input("Please enter the Property value eg100000: "))
    monthly_interest_rate = float(input("please Enter the interest rate eg 7: "))
    repayment_months = float(input("Please enter the number of months you intend to pay back , eg 120: "))

    # re-assigning the variable to simplify equation readability
    P = property_value
    i = monthly_interest_rate /12
    n = repayment_months

    # Calculation used in this program x = (i.P)/(1 - (1+i)^(-n))
    # alternate calculation - repayment = i*P *math.pow((1+i),n) / math.pow((1+i),n) (has the same results)

    # Bond repayment calculation with python appropriate syntax
    repayment = i * P / (1 - math.pow((1 + i), -n))
    repayment = round(repayment, 2)

    # Display
    print(" ")
    print(f"You will have to R{repayment} per month")
