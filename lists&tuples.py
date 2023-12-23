friends=['chakri','mohan','ramesh','dawood',2,10.15]# we can keep any type of value in the list eithe it is integer or strings or floating point value 
print(friends)
# we can also list the iteams seen in the below it called as list indexing 
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
# as we can see in the below out when ever we want to access any member in the list we can access with it index 
# list slicing 
cars=['mahindra','audi','bmw','porche']
print(cars[0:3]) # in this when we print 0 to 3 it will only print from 0 to 2 because it will skip the 3rd one in the list 
print(cars[-2:]) # when we have to access the list form (-) it will print in the reverse order 
# there are some list methods list below
# 1.list.sort()
# 2.list.reverse()
# 3.list.append()
# 4.list.insert()
# 5.list.pop()
# 6.list.remove() let us see one by one in detail
# let us consider the following the list 
# list.sort()
list=[1,8,7,2,21,15]
list.sort()
print("list is sorted in order:",list) # we can see in the output the list is updated in order vise
# list .reverse ()
list=[1,8,7,2,21,15]
list.reverse()
print("list is reversed :",list)
# list.append()
list=[1,8,7,2,21,15]
list.append(25) # it will add 25 at the end of the list
print("list is append :",list)
# list.insert()
list=[1,8,7,2,21,15]
list.insert(3,9) # it will add the value at 3 is index and 9 is the value to be added first we have to select the index from left and then we have to give the value to be inserted at the index which you have given
print("list is inserted :",list)
# list.pop()
list=[1,8,7,2,21,15]
list.pop(3) # in this which value at index 3 it will be deleted 
print("list is pop:",list)
# list.remove()
list=[1,8,7,2,21,15]
list.remove(15)
print("list  value is removed  :",list)

# let us come to next method is tuple. tuple is nothing but it is datatype which we cannot be changed let us create a tuple()
b=(1,2,4,5,7,8)
print(b[4])
# b[0]=24 # we we want to update any new value it throws a error because we cannot update value in the list
print(b)
# the are two methods in typle 
# a.count()
# a.index()
b=(1,2,4,5,7,8,2,3,2,3,2,4,5,5,6)
print(b.count(4)) # we can see the output it will count the same number of values in the list
# a.index()
b=(1,2,4,5,7,8)
print(b[4]) # it will give the value which is at index 4 which is 7
