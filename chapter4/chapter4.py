foods = ["pizza", "taco", "dim sum", "sushi"]

print(foods[1])

#for PLACEHOLDER in THE_LIST_WE_WANT_TO_LOOK_AT:
    # this is a code block
    # this code block
    # will run every item in the list
for food in foods:
    print(
        f"I like to eat {food}")
    print(type(food))

print("loop is over")     


for food in foods:
    
    if food == "dim sum":
        break
    print(f" Ilike {food} because they are yummy")


for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My No {index + 1} food is {food.title()}")

# loop of the index
print(list(range(len(foods))))
print(len(foods))

my_string = "Steve"
my_string = my_string + " smells like teen spirit"
print(my_string)

my_tup = 1, 2
print(type(my_tup))
my_tup = (1,2)
print(type(my_tup))
print(my_tup)

print(my_tup[1])

for num in my_tup:
    print(num)

my_tup = my_tup + (3,4)
print(my_tup)

# Slicing
my_string = "Hey Guy Let Learn Python"
my_list = ["pizza", "tacos", "dim sum", "sushi"]

print(my_string[1:4])
print(my_string[4:7])
print(my_string[::])
print(my_string[::2])
print(my_list[1:4:2])
print(my_list[-1])

print(my_list[1])

deck = ["p", "m", "g" "c"]
print (deck[1] )#+ deck[5])

deck = ["p", "m", "mt", "c"]
deck[3] = "ch"
deck=deck.reverse()
print(deck)

#sorted(deck)
#print(deck)

#my_list = ["ch", "ch", "hot", "bol", "ch", "ma"]
#my_string = ""
#for index, object in enumerate(my_list):
#my_string += object + " "
#if index == e or index == 4:
#    my_string += "and "
#print(my_string)


my_list = [1,3.0,["a","b",["A", "B", "C"], "d"], "John"]
print(my_list [2][2][0])
for member in my_list:
    if isinstance(member, list):
        for m in member:
            if isinstance(m, list):
                print(m, end=" ")


a = 10
if(a==10):
    print("\n", a)

