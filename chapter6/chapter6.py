# From text book
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

person_0 = {'first_name' : 'Catherine', 'last_name' : 'Wong', 'age' : '47', 'city' : 'las vegas'}

favorite_number = {
    'jack' : 12, 
    'bambam' : 8, 
    'bob' : 17, 
    'gordon' : 11, 
    'enos' : 12
    }
print(favorite_number)

programming_words = {
                    'print' : 'to show info', 
                    'for ... in' : 'loop',
                    'if' : 'conditional statement',
                    'reverse' : 'put list in reverse order',
                    'sorted' : 'put list in order'
                    }
for programming_word in programming_words:
    print(programming_word.title() + " : " + "\n" + "\t" + programming_words [programming_word].title() + "\n")

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
 }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi "+ name.title() + 
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, plesae take our poll!")

for name in sorted(favorite_languages.keys()):
    print((name.title() + ", thank you for taking the poll."))

programming_words = {
                    'print' : 'to show info', 
                    'for ... in' : 'loop',
                    'if' : 'conditional statement',
                    'reverse' : 'put list in reverse order',
                    'sorted' : 'put list in order',
                    'del' : 'remove list'
                    }
for programming_word in programming_words:
    print(programming_word.title() + " : " + "\n" + "\t" + programming_words [programming_word].title() + "\n")

print("New programming word list")
for programming_word in programming_words.values():
    print (programming_word) 

rivers = {
        'nile': 'egypt', 
        'yellow' : 'china', 
        'missouri' : 'usa'
        }
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
 }    

poll_takers = ['jen', 'phil', 'jack', 'po']
for poll_taker in poll_takers:
    
    if poll_taker in favorite_languages.keys():
        print("Hi  " + poll_taker.title() + 
              ", thank you for taking the poll!")
    else:
        print("Hi " + poll_taker.title() + ", please take the poll!")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)

 aliens = []

 for alien_number in range(30):
     new_alien = {'color': 'green', 'points' : 5, 'speed': 'slow'}
     aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")
      
print("Tptal number of aliens: " + str(len(aliens)))

print(person_0)
person_1 = {'first_name' : 'john', 'last_name' : 'sanders', 'age' : 44, 'city' : 'springvile'}
person_2 = {'first_name' : 'elain', 'last_name' : 'rhodes', 'age' : 43, 'city' : 'corona'}

persons = [person_0, person_1, person_2]
print(persons)

pi = {'kind' : 'dog', 'owner' : 'catherine'}
puss = {'kind' : 'cat', 'owner' : 'sony'}
krypto = {'kind' : 'dog', 'owner' : 'superman'}
pets = [pi, puss, krypto]

print(pets)
#for k in pets['kind']:
#   print(k)

favorite_places = {
    'luke' : ['las vegas', 'beaverton', 'portland'], 
    'catherine' : ['hong kong', 'london', 'tokyo'], 
    'enoch' : ['kahuku', 'hong kong', 'taipei']}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())

print(favorite_number)

favorite_number['bambam'] = [8,39]
favorite_number['jack'] = [12,33]
favorite_number['bob'] = [17,1]
favorite_number['gordon'] = [11,31]
favorite_number['enos'] = [12,6]
for name, number in favorite_number.items():
    print(name.title() + "'s favorite numbers are:")
    for numbers in number:
        print("\t" + str(numbers))


my_dict = {}
my_dict = dict()

my_dict = {
    "key":"value"
}

my_dict = dict(key="value")

steve = {
    "name" : "Steve",
    "weight" : 155.5,
    "height" : 70,
    "foods" : ["country fried steak", "fried chicken", "collards"],
    "ice_cream" : {
    "vanilla" : False,
    "chocolate" : True,
    "coffee" : False,
    "soup" : "chicken"
    },
    10 : "this has an interger key"
}
# name_of_dict[KEY]
print(steve.get("candies", "No Candy List"))
print(type(steve[10]))

steve["name"] = "Joe"
print(steve)

#change value in list
my_list = [1,2,3]
my_list[1] = "WOW"
print(my_list)

# add value
steve.update(
    {
    "candies" : ["snickers", "mars", "m&ms"]})

print(steve)

del steve["candies"]
print(steve)

#looping over dict
for key in steve:
    print(key)
    print(type(key))
    print(steve[key])

print(steve.values())
for value in steve.values():
    print(value)
    print(type(value))

print(steve.items())

for key, value in steve.items():
    print(key, end= " ")
    print(value)

for key, value in steve.items():
    if isinstance(value,list):
        print(f"The list is at {key}")


my_dict = {
    "name" : "troy",
    "awards":{
    "man_of_the_year" : 1997,
    "super_bowl_mvp" : "xxvii",
    "superbowls" : ["xxviix", "xxviii", "xxx"],
    }
}
#del my_dict[name]
#print(my_dict.get("name",0))


my_dict = {
    "name": "troy aikman",
    "position" : "QB",
    "team":"Dallas Cowboys",
    "age" : 54,
    "weight" : 220,
    "superbowls":["xxvii", "XXviii", "xxx"],
    "awards" : {
    "super_bowl_mvp" : "xxvii",
    "probowl":[1991,1992,1993,1994,1995,1996],
    "man_of_the_year":1997
        }
}
for key in my_dict:
    if key > "position":
        print(key, end=" ")


for value, key in my_dict.items():
    if value == 54:
        print("Old", end="")
    if value == "age":
        print("54", end="")


my_dict['awards']['probowl'].reverse()
print(my_dict['awards']['probowl'].pop(2))

my_dict.update({"age":14})
print(my_dict["age"])

print(my_dict.get("awards","age")["probowl"][len(my_dict["position"])])

a_list=[]
for k, v in my_dict["awards"].items():
    if k == "super_bowl_mvp" or k == "man_or_the_year":
        a_list.append(v)
print(a_list)

print(my_dict['name'] + " has won", len(my_dict["superbowls"]))