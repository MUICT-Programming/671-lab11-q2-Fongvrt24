# YOUR CODE HERE
n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(int(input()))
for i in range(n):
    list2.append(int(input()))
def summation (a,b):
    listsum=[]
    global n 
    for i in range(n):
        listsum.append(a[i]+b[i])
    return listsum
listsum=summation(list1,list2)
def find_min_max(a):
    min=a[0]
    max=a[0]
    for i in a:
        if i<min:
            min=i
        else:
            continue
    for i in a:
        if i>max:
            max=i
        else:
            continue
    min_max = (min,max)
    return min_max
print(summation(list1,list2))
print(find_min_max(listsum))
