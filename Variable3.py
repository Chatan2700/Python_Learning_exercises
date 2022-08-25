#Global Variables

x = "Awesome" #Global

def myfunc(): #Define function
    x = "Fantastic" #Local
    print("Python is " + x)
    print("Python is {}" .format(x)) #Another way of do it

myfunc() #Call the function

print("Python is " + x)

#The global Keyword

def my_func():
    global y #Declare a global variable inside a func
    y = "Fantastic"

my_func()
print("Python is " + y)


# To change a global variable inside of a function

z = "Cool"

def my_Fun():
    global z
    z = "Amazing"

my_Fun()
print("Python is " + z)

