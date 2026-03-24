# Write a program to print third, fifth and seventh element from a list using enumerate 
#function. 
list1=[234,34,45456,563,453,563,543,56,43]
for i,item in enumerate(list1):
    if i==2 or i==4 or i==6:
        print(item)