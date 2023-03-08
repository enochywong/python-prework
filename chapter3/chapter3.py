my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))

# index    0  1 2 3    4
numbers = [2,6,10,12.5,0]# this is also comment
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print(numbers[1]*2.5)
print(type(numbers[1]*2.5))

# name of the list we want t o index 

print(type(numbers[3]))
print(type(numbers[3]))

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x= 12
y= 15.5
z= "Z"

random_list = [x,y,z,]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

foods.append("cheeseburger")
print(foods)

foods.insert(0,"pho")
print(foods)

foods.remove("pho")
print(foods)

foods.remove("cheeseburger")
print(foods)

print(foods)

foods.append("pizza")
print(foods)

foods.remove('pizza')
print(foods)

foods.remove('pizza')
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
del foods[1]
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.pop())
print(foods)
print(foods.pop())

foods = ["pizza", "tacos", "dim sum", "sushi"]

print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(sorted(foods))
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.reverse()
print(foods)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() +", thtat was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n)")

print("Thank you, everyone. That was a great magic show!")

pizzas = ['magarita', 'hawaiian', 'meat']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("\nI really like pizza!")

animals = ['horse', 'zebra', 'pony']
for animal in animals:
    print(animal)
print("\nAll these animals have four legs.")

for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
    # squares.append(square)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

#numbers =[]
#for number in range(1,21):
#    print(number)

numbers = list(range(1,1000001))
print(sum(numbers))
print(max(numbers))
print(min(numbers))

odd_numbers = list(range(1,21,))
for odd_number in odd_numbers:
    print(odd_numbers)

for value in range(1,21,2):
    print(value)

odd_numbers = []
for value in range(-1,21):
    odd_number = value + 2
    odd_numbers.append(odd_number)
    print(odd_number)

odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)

three_times = list(range(3,31,3))

print(three_times)

cubes = [value**3 for value in range(1,11)]
#for value in range(1,11):
 #   cube = value**3
  #  cubes.append(cube)
print(cubes)


players= ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

my_foods.append('fries')
friend_foods.append('cake')

print("my favorite offds are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("The first three my favoirte foods are: ")
for my_food in my_foods[:3]:
    print(my_food.title())

print("The first three my favoirte foods are: ")
for my_food in my_foods[1:4]:
    print(my_food.title())

print("The first three my favoirte foods are: ")
for my_food in my_foods[-3:]:
    print(my_food.title())    

friend_pizzas = ['cheese', 'hawaiian', 'meat', 'margarita']
print(friend_pizzas)
friend_pizzas.append('peperoni')
print(friend_pizzas)

original_pizzas = friend_pizzas[:]
print(original_pizzas)

friend_pizzas.append('fruit')
print(friend_pizzas)

print("My favorite pizzas are:")
for original_pizza in original_pizzas[:]:
    print(original_pizza.title())

print("My friend favorite pizzas are:")
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza)

for my_food in my_foods [:]:
    print(my_food)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

basic_foods = ('rice', 'pasta', 'potato', 'bread', 'meat')
for basic_food in basic_foods:
    print(basic_food)

# basic_foods [0] = 'water'

basic_foods = ('salad', 'cheese', 'rice', 'pasta', 'potato')
for basic_food in basic_foods:
    print(basic_food)


