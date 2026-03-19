#raise is used to manually create an error
try:
    num=int(input("Enter a number:"))
    if num<0:
        raise ValueError("Number can not be negative")

    print("Number is:",num)

except ValueError as e:
    print("Error",e)