#Used to modify a variable outside function
x=10
def change():
    global x
    x=32
    
change()
print(x)