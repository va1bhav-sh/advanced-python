from functools import reduce

#map() Apply function to every item 
nums=[1,2,3,4]
result=list(map(lambda x:x*x,nums))
print(result)

#filter() Select some items 
n=[1,2,3,4,5,6]
final=list(filter(lambda x:x%2==0,nums))
print(final)\
    
#reduce() Combine all values
l=[1,2,3,4]
op=reduce(lambda a,b:a+b,nums)
print(op)