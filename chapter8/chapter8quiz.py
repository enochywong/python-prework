def rafiki(lion):
    print(lion + " " +
          "Oh yes, the past can hurt.\
            But the way I see it,\
                you caneither run from it or learn from it")
rafiki('iba')    


def dory(fish, last):
    if last > 10:
        print("Who are you?", end=" ")
    else:
        if fish=="Nemo":
            print("Just keep swimming", end=" ")
        
        else:
            print("I don't know you", end=" ")
    
#print(dory("Nemo", 90))


def dory(fish, last):
    my_string= ("The" +{fish} + "that blooms" + "in " + {last})
    return my_string
    
#print(dory("Nemo", "Marlin"))

def see(name, age, species='human'):
    print(name,age,species)

see("Ariel", 16)

x=5
def some_func(x):
    print(x, end=" ")
print(x, end=" ")
some_func(1)
x=x-1
print(x,end=" ")
some_func(1)

def fun(num):
    return num + 5
def funb(num):
    return num*2
print(fun(5) + funb(5))