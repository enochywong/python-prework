#8-1
def display_message():
    """Display a simple message."""
    print("I'm learning functions in this chapter.")

display_message()

#8-2
def favorite_book(title):
   """Display favorite book"""
   print("One of my favorite books is " + title.title() + ".")

favorite_book('Alice in Wonderland')

#8-3
def make_shirt(size, message = 'I love Python.') :
    """Display information about print t-shirt"""
    print("\nShirt Size: " +size.upper() + " - shirt text: " + message.title())

make_shirt('L')
make_shirt('M')
make_shirt(message = 'WOW!', size = 'S')

#8-5
def describe_city(city, country = 'Taiwan'):
    """Display inforamtino about city and country"""
    print(city + " is in " + country + " .")

describe_city('Taipei')
describe_city('Yilan')
describe_city(city = 'Madrid', country = 'Spain')

#8-6
def city_country(city, country):
    """Return City and Country"""
    country_info = city + ', ' + country
    return country_info.title()

city_info = city_country('santiago', 'chile')
print('"' + city_info + '"')
city_info = city_country('las vegas', 'united states')
print('"' + city_info + '"')
city_info = city_country('paris', 'france')
print('"' + city_info + '"')

#8-7
def make_album(artis_name, album_title, number_of_tracks = ''):
    """Build a dictionary descirbing a music album"""
    album_info = {'name' : artis_name, 'title' : album_title, 'tracks' : number_of_tracks} 
    return album_info

artis_album = make_album('boyz II men', 'christmas', 10)
print(artis_album)
artis_album = make_album('mariah carey', 'butterfly')
print(artis_album)
artis_album = make_album('BTS', 'butter')
print(artis_album)

#8-8

def make_album(artis_name, album_title, number_of_tracks = ''):
    """Build a dictionary descirbing a music album"""
    album_info = {'name' : artis_name, 'title' : album_title, 'tracks' : number_of_tracks} 
    return album_info

while True:
    print("\nEnter the name of the artist:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Enter album name: ")
    if a_title == 'q':
        break

    a_tracks = input("Enter number of tracks: ")
    if a_tracks == 'q':
        break

    artis_n_album = make_album(a_name, a_title, a_tracks)
    print(artis_n_album)

#8-9

def show_magicians(magicians):
    """Print magicians' name"""  
    for magician in magicians:
        magicians_name = "Magician: " + magician.title() + "!"
        print(magicians_name)

#magicians = ['copperfield', 'blain', 'Lim']
#show_magicians(magicians)

#8-10 ?????????

def make_great(magicians):
    """Modify magician name by adding The Great"""
    while magicians:
        the_great = magicians.pop() + " the Great"
        print(the_great)
        great_magicians.append(the_great)
          
      
magicians = ['copperfield', 'blain', 'Lim']
great_magicians = []
show_magicians(great_magicians)
print(great_magicians)
#8-11???????

#8-12
def sandwich_type(*ingridents):
    """Print the list of sandwiches."""
    print("\nSandwich with the follwoing ingreidents:")
    for ingrident in ingridents:
        print("- " + ingrident)

sandwich_type('tomato', 'ham')
sandwich_type('turkey', 'cheese')
sandwich_type('beef', 'pickles')

#8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('enoch', 'wong',
                             location='utah state university',
                             field='marketing', honor="cum laude")
print(user_profile)

#8-14
def build_car_profile (manufacture, model, **car_info):
    profile = {}
    for key, value in car_info.items():
        profile['manufacture_name'] = manufacture
        profile['model_name'] = model
        profile[key] = value
    return profile

car_profile = build_car_profile('honda', 'pilot', 
                                color = 'grey',
                                cylinder = 4,
                                heated_seats = True)

print(car_profile)

test = ['car', 'cat', 'dog']
check = []
tested = test.pop(0) + " again"
print(tested)

#lesson
# def NAME_OF_FUNCTION(PARAMETERS):
    #THESE LINE
    #belong
    #to the code block
    #for the function

def hello():
    print("Hello")
    # wont print, just a function

print(hello()) # now will print but will print 'Hello' and 'None'

def hello(name, age):
    print(f"Hello {name} you are {age} years old")
    
hello("Kevin", 23) 


def say_hello(name, age):
    print(f"hellp {name} you are {age} years old")

def say_goodbye():
    print("Goodbye")

def greet_back(feeling):
    if feeling == "good":
        print("Awsone I feel good too")
    elif feeling == "bad":
        print("I am so sorry")
    elif feeling == ("stressed"):
        print("Coding can be hard to learn")
    else:
        print("well, have a good day!")

#Drive Code
while True:
    response = input("What do you want to do? Say hello [H] Say goodbye [G] talk to me [T] or quit [Q]")
    if response.lower() == 'q':
        say_goodbye()
        break
    elif response.lower() == 'h':
        name = input("what is your name? ")
        age = input("What is your age? ")
        say_hello(name, age)
    elif response.lower() == 'g':
        say_goodbye()
    elif response.lower() == 't':
        feeling = input("how are you today?")
        greet_back(feeling)
    else:
        print("invalid input")

def my_function(num):
    while num < 10:
        print(num)
        if num == 6:
            return # once hit return it will stop
        num +=1


