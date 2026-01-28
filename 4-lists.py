mylist = ["apple", "banana", "cherry", "apple", "cherry"]
mylista = [ 1, 2, 3, 4, 5 ]

print(len(mylist)) # Output: 5
print(type(mylist)) # Output: <class 'list'>
print(type(mylista[0])) # Output: <class 'int'>

print(type(mylist[0])) # Output: <class 'str'>
print(mylist[0]) # Output: apple
print(mylist[1]) # Output: banana
print(mylist[2]) # Output: cherry
print(mylist[3]) # Output: apple
print(mylist[4]) # Output: cherry
print(mylist[::2]) # Output: ['apple', 'cherry', 'cherry']
print(mylist[-1]) # Output: cherry
