#4-1
pizza_list = ['pepperoni', 'sasusage', 'mushroom', 'pineapple']
for pizza in pizza_list:
    print(pizza)

for pizza in pizza_list:
    print(f"I like {pizza} pizza")


#4-2
animal_list = ['turtle', 'frog', 'fish']
for animal in animal_list:
    print(animal)

for animal in animal_list:
    print(f"A {animal} would make a great pet")
print("\nAll of these animals are green")

#4-3
for numbers in range(1,21):
    print(numbers)

print("\n")

#4-4
list_to_million = list(range(1, 1000001))
print(len(list_to_million))

#4-5
print(min(list_to_million))
print(max(list_to_million))
print(sum(list_to_million))
print("\n")

#4-6
for odd_numbers in range(1,21,2):
    print(odd_numbers)

print("\n")

#4-7
for multiple_of_threes in range(3,31,3):
    print(multiple_of_threes)
    
print("\n")

#4-8
cubes = [value**3 for value in range(1,11)]
print(cubes)

print("\n")

#4-9
#same as 8

#4-10
print("The first three items in the pizza list are:")
print(pizza_list[0:3])
print("\n")

print("The items in the middle of the pizza list are:")
print(pizza_list[1:3])
print("\n")

print("The last items in the pizza list are:")
print(pizza_list[-3:])
print("\n")

#4-11
friends_pizza = pizza_list[:]
pizza_list.append("ham")

print("My pizzas are:")
for my_pizza in pizza_list:
    print(my_pizza)

print("\n")
print("friends pizzas are:")
for friend_pizza in friends_pizza:
    print(friend_pizza)


#4-12
#same as above

#4-13 Tuples
buffet = ("rice", "meat", "noodles", "soup", "fruit")
for food in buffet:
    print(food)
buffet[0] = "brown rice"