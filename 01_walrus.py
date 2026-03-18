#It lets you assign a value to a variable AND use it in the same expression.

#Without walrus operator
# data=input("Enter:")
# while(data!="quit"):
#     print(data)
#     data=input("Enter:")

#With walrus
while(data:=input("Enter:")) !="quit":
    print(data)