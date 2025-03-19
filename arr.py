from array import array

array_num= array('i', [1,2,3,4,5])
li=[12,14,23,54]
array_num.reverse()
print(array_num)
x=array_num.count(4)
print(x)
array_num.extend(array_num)
print(array_num)
array_num.fromlist(li)
print(array_num)

c=array_num.tolist()
print(c)

array_num.insert(4,2000)
print(array_num)

x=array_num.index(3)
print(x)
array_num.remove(5)
print(array_num)

gig=array_num.tobytes()
print(gig)