#Chatper 3

#3-1
names = ['ken', 'mich', 'froppy']
print(names[0])
print(names[1])
print(names[2])

#3-2
print(f"{names[0].title()} is learning python")

#3-3
print(f"{names[1].title()} goes for a walk")

#3-4
family = ['dad', 'mom', 'brother', 'sister']
print(f"{family[0]}, you are invited")

#3-5
print(f"{family[0]}, cannot make it anymore")
family[0] = 'pops'
print(f"{family[0]}, you are invited")

#3-6
family.insert(1, 'friend')
family.insert(0, 'friend 2')
family.append('friend 3')
print(family)

#3-7
family.pop()
family.pop()
family.pop()
family.pop()
family.pop()
print(family)
family.remove('friend 2')
family.remove('pops')
print(family)

#3-8
locations = ["San Francisco", "Pheonix", "Houston", "Dallas", "New York"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

#3-9
print(len(family))

#3-10
