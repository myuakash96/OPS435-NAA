def hello():
    print('Hello World')
    print('Inside a Function')
    return

my_stuff = hello()
print('Stuff return from hello():',my_stuff)
print('the object my_stuff is of type:',type(my_stuff))
