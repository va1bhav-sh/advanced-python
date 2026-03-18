#Varirable Type Hints
age : int =25
name : str = "Vaibhav"
price : float =99.4
is_active : bool = True

#Function Type Hints
def greeting(name:str) -> str:
    return f"Hello, {name}!"

print(greeting("Vaibhav"))