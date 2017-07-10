def divide_numbers(num1, num2):
    """This function checks if one number can be divided to other without remnant"""
    if isinstance(num1, int) and isinstance(num2, int):
        result = num1 % num2
        if result == 0:
            if num2 != 4:
                print("Number {} can be divided to number {} without remnant".format(num1, num2))
            else:
                print("Can be divided to 4")
        else:
            print("Remnant is: " + str(result))
    else:
        raise Exception("Wrong arguments passed to function")

check = int(input("please type first number: "))
num = int(input("please type second number: "))

divide_numbers(check, num)
