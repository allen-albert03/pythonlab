list=[3,56,12,98,43,23]
print(list)

print("The largest in the list is ",max(list))

print("The sum of all elements in the list is ",sum(list))

evenlist=[i for i in list if i%2==0]
print("Even numbers are: ",evenlist)

greatlist=["over" if i>50 else i for i in list]
print("Replaced by over which are greater than 50",greatlist)

print("The smallest in the list is ",min(list))

list.reverse()
print(list)

list.append(500)
print("New list is : ",list)

list.sort()
print("Sorted list are: ",list)
