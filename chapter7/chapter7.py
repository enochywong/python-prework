car = input("What kind of car would you like to rent?")
print(f"Let me see if I can find you a {car}.")

group_size = input("How many people in your dinner group?")
group_size = int(group_size)

if group_size >= 8:
    print("Pleae wait.")
else:
    print("Your table is ready.")

number = input("Enter a number and I will tell you if the number is a multiple of 10:")
number = int(number)

if number % 10 == 0:
    print("Your number is a multiple of 10.")
else:
    print("Your number is not a multiple of 10.")

current_number = 1
while current_number <=5:
    print(current_number)
    current_number +=1

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
# message = input(prompt)

# if message != 'quit':
#    print(message)

#active = True
#while active:
#    message = input(prompt)

#    if message == 'quit':
#        active = False 
#    else:
#        print(message)

prompt ="\nWhat topping would you like to add to your pizza?"
prompt += "\n(Enter 'quit' when you are done adding topping)"

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print("Adding " + topping.title() + "  to your pizza.")
print("Thank you for adding your toppings! Your pizza will be ready in 20 min.")


prompt ="\nWhat's the age of the person?"
prompt +="(Enter 'quit' when you are done)"

count = 1
while count <4:
    age=(input(prompt))
    if age == 'quit':
        break
        
    if int(age) <3:
        print("Tiket is free for age 3 and under.")
    elif int(age) <=12:
        print("Ticket cost for age from 3 to 12 is $10.")
    else:
        print("Ticket cost for age 13 and older is $15")
    count += 1
    

sandwich_orders =['blt', 'pastrami', 'beef', 'pastrami','egg', 'chicken', 'pastrami','tuna']
finished_sandwiches = []

print("Sorry, we are out of Pastrami Sandwich.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making_sandwiches = sandwich_orders.pop()

    print("I made your " + making_sandwiches.title() + " sandwich")
    finished_sandwiches.append(making_sandwiches)
print("List of made sandwhiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " sandwich")

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name?")
    response = input("If you could visit one place in the world, where would you go?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
           polling_active = False

print("\n----Vacation Spot Polling Result---")
for name, response in responses.items():
    print(name + " would like to go to " + response + " for vacation.")


# Lesson Video
# The while loop
#while boolean or boolean expression:
    #code block
    #to run while
    #condition is true

# You must be over 5 feet to ride my ride# 
# I have a magic potion that will let you grow one inch everytimg you use it!
height = int(input("What is your height in inches?"))
while height < 60:
   height += 1
   if height < 58:
    continue
    print(f"You are {height} inches tall \n and too short to ride!")
    print("Drink my magic potion")
    if height == 58:
        break
    
print("Thanks for coming")


while True:
    response = input("what do you want to do? Say hi [h], Say goodbye [g], or Quit [q]?")
    if response.lower() == "h":
        print("hellp")
    elif response.lower() == "g":
        print("goodbye")
    elif response.lower()=="q":
        break
    else:
        print("invalid option")

age = int(input("age"))
while age < 20:
    age += 1
    print(age)

while False:
    


 





