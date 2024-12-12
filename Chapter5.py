#5-1
nfl_team = '49ners'

print("Is nfl_team == '49ners' I predict True")
print(nfl_team == '49ners')

print("Is nfl_team == 'GB' I predict False")
print(nfl_team == 'GB')

#5-2
print("########question 2#########")
print("\n")
age = 18
print("is 18 in between 6 and 20?")
print(age > 20 or age < 6)
alphabet = ['a', 'b', 'c']
print("Is 'd' in alphabet?")
print('d' in alphabet)
print("Is 'b' in alphabet?")
print('b' in alphabet)
print("\n")
#5-3
alien_color = 'red'
if alien_color == 'green':
    print("Player earned 5 points!")
else:
    print("No points earned.")
print("\n")

#5-4
if alien_color == 'green':
    print("Player earned 5 points!")
else:
    print("Player earned 10 points!")
print("\n")

#5-5
if alien_color == 'green':
    print("Player earned 5 points!")
if alien_color == 'yellow':
    print("Player earned 10 points!")
else:
    print("Player earned 15 points!")

#5-6
age = 18
if age < 2:
    print("Person is a baby")
elif age > 2 and age < 4:
    print("Person is a toddler")
elif age > 4 and age < 13:
    print("Person is a kid")
elif age > 13 and age < 20:
    print("Person is a teenager")
elif age > 20 and age < 65:
    print("Person is an adult")
else:
    print("Person is an elder")

#5-7
favorite_fruit = ['watermelon', 'banana', 'orange']

if 'watermelon' in favorite_fruit:
    print(f"You really like watermelon")

#5-8
user_names = ['admin', 'kenn', 'mich' 'tree', 'chair']

for element in user_names:
    if element == 'admin':
        print(f"Hello {element}, would you like a status report?")
    else:
        print(f"Hello {element}, thank you for logging in.")

print("\n")

#5-9
if user_names:
    for element in user_names:
        if element == 'admin':
            print(f"Hello {element}, would you like a status report?")
        else:
            print(f"Hello {element}, thank you for logging in.")
else: 
    print("We need to find some users")
print("\n")

#5-10
current_users = ['aaa111', 'bbb222', 'ccc333']
current_users_lower = [x.lower() for x in current_users]
new_users = ['ddd444', 'eee555', 'cCC333']
new_users_lower = [x.lower() for x in new_users]


for n_element in new_users_lower:
    if n_element not in current_users_lower:
        print("User name is available")
    else:
        print("User name used, please enter new user name")

print("\n")

#5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in numbers:
    if element == 1:
        print(f"{element}st")
    elif element == 2:
        print(f"{element}nd")
    elif element == 3:
        print(f"{element}rd")
    else:
        print(f"{element}th")

       