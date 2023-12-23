# there are three types of strings are their 
# single quoted 
# double quoted 
# thriple quoted let us see an example 
# string slicing 
name="arsalaan"
print(len(name))  #we can see the length of the string using len()
#in the below example we have created a variable boom int that the index is start from 0 to 5 means it will count the letters from 0 to 5
boom=name[1:3]
print(boom)
# slicing with skip value 
man="amazing"
a=man[0:6:5]
print(a) # in this example we have seen the skip value 
# other advance string techniques 
word="manpower"
c=word[:5] # it will automatically count from index 
print(c)
#string concatination 
greetings="\ncongratulations you have selected in microsoft "
name="arsalaan"
print(name+greetings)
#string functions 
#there are six types of string functions are there 
# 1.string len()
# 1.string.endwith()
# 1.string.count()
# 1.string.capitalize()
# 1.string.find()
# 1.string.replace() let us see onre by one 
story="once upon a time there was developer his name was sk arsalaan who was working on microsoft"
print(story.endswith("microsoft"))
# sting .cont()
story="once upon a time there was developer his name was sk arsalaan who was working on microsoft"
print(story.count("n"))
# string .capitalize()
story="once upon a time there was developer his name was sk arsalaan who was working on microsoft"
print(story.capitalize())
# string .find()
story="once upon a time there was developer his name was sk arsalaan who was working on microsoft"
print(story.find("microsoft"))
# string .replace()
story="once upon a time there was developer his name was sk arsalaan who was working on microsoft"
print(story.replace("microsoft","Amazon"))
# so we have seen all the functions have different purpose in the python 




