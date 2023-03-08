car = 'subaru'
print("is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print (car == 'audi')

food = 'rice'
print("is food 'rice'? I predict True.")
print(food == food)

name = 'joyce'
print("I think your name is Joyce. That's ture, right?")
print(name == 'joyce')

name = 'joyce'
print("I think your name is Kate. That's ture, right?")
print(name == 'kate')

sport = 'Soccer'
if sport.lower() == 'soccer':
    print("How do you like the 2022 World Cuo?")
if sport.lower() != 'soccer':
    print("You should start watching. It's a great sport")


num_1 = 8
num_2 = 12

print((num_1 == 7) or (num_2 > 11))

list = ['trach', 'can', 'bin', 'garbage']
print('food' not in list)

age = 64

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
        price = 10
else:
    price = 10

print("Your admisssion cost is $" + str(price) + ".")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

alien_color = 'yellow'
if alien_color == 'green':
    print("\n You just earned 5 points")
elif alien_color == 'yellow':
    print("\nYou just earned 10 points")
else:
    print("\nYou just earned 15 points.")

age = 17
if age < 2:
    print("\nThe person is a baby.")
elif (age >=2) and (age <4):
    print("\nThe person is a toddler.")
elif (age >=4) and (age <13):
    print("\nThe person is a kid.")
elif (age >=13) and (age <20):
    print("\nThe person is a teenager.")
elif (age >=20) and (age <65):
    print("\nThe person is a adult.")
else:
    print("\nThe person is a elder.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping +".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza.")

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ['peter', 'eric', 'pele', 'messi', 'mitoma']
new_users = ['Messi', 'mitoma', 'jack', 'bam', 'yellow']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("The username " + new_user + " is not available please select a differnt user name.")
    else:
        print(new_user + ", Welcome back!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")

# Boolean can be two things ON or OFF true or False Yes or No
my_bool = True
print (my_bool)
my_bool = False
print(bool([]))

x = 10
print(5 < x <20)

# can do it for letters
letter = 'c'

print(letter > "b")
print(ord("A"))

x = 10
y = 10
z = 20

print(x == 10 and z == 10)

x = 8
y = 9
print(x != y)
print(not x == y)

# if BOOLEAN OR BOOLEAN EXP:
    # code block
    # for if true
# else:
    # for the if false code block

height = 75

# Must be 5 feet tall to ride my ride
# Must be under 6 feet tall to ride

if height < 60:
    print("You are too short")
    print("I am sorry but get off of my ride!")
elif height > 72:
    print("You are too tall!")
    print("Get off my ride!")
else:
    print("Enjoy the Ride!")
print("Thanks for visiting")    

print(x == y)

number = 8
if True:
    print("Number is less than 8")

x = 5
y = 10
i = "5"
j = "10"
if x ==i and x != y:
    print("Blackbird", end=" ")
else:
    print("singing", end=" ")
print("in the", end=" ")
if x <int(j) or i ==j:
    print("dead", end=" ")
else:
    print("of night", end=" ")