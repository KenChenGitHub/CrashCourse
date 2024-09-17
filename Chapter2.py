#Chapter 2 

#2-1 Assign a message to a variable, and then print that message

message = "Hello, Python Crash Course"
print(message)

#2-2 
var1 = "Hello"
print(var1)
var1 = "No Hello"
print(var1)

#2-3
var1 = "KC"
message = f"Hello {var1}, would you like to learn some Python today?"
print(message)

#2-4
var1 = "ken"
print(var1.lower())
print(var1.upper())
print(var1.title())

#2-5
print('Ken\'s park')

#2-6
famous_person = "Ken"
print(f"{famous_person}'s park")

#2-7
var1 = "   KEN   "
print(f"\tvar1")
var1 = var1.rstrip().lstrip()
print(var1)

#2-8
filename = "python_notes.txt"
print(filename.removesuffix('.txt'))