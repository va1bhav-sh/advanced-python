#Short way to create lists

#Normal way:
# list1=[1,7,12,11,22]
# list2=[]
# for item in list1:
#     if item>8:
#         list2.append(item)

# print(list2)

#Short Way
list1=[1,7,12,11,22]
list2=[i for i in list1 if i>8]
print(list2)