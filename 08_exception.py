#Exception handling = making your program smart enough to handle user mistakes
try:
    num=int(input("Enter a number: "))
    result=100/num
    
except Exception as e:
    print(e)
    
except ZeroDivisionError:
    print("Number can not be zero")
    
else:
    print("Result is:",result)

finally:
    print("Program Ended")
