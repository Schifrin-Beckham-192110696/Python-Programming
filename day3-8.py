a=int(input("Enter no of elements: "))
list1=[]
for i in range(0,a):
    c=int(input("Enter the element: "))
    list1.append(c)
print("list of elements in list1 : ",list1)

d=int(input("Enter no of elements: "))
list2=[]
for i in range(0,d):
    e=int(input("Enter the elements: "))
    list2.append(e)
print("list of elements in list2 : ",list2)

sorted_list =[]
while list1 and list2:
    if list1[0] <  list2[0]:
        sorted_list.append(list1.pop(0))
    else:
        sorted_list.append(list2.pop(0))
sorted_list += list1
sorted_list += list2
print(sorted_list)
