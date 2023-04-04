''''
Make a function that will return a greeting statement that uses an input; your program should return,
"Hello, <name> how are you doing today?".
[Make sure you type the exact thing I wrote or the program may not execute properly]
'''

nome = input("What's your name? ")

def greet(name):
    return ("Hello, {} how are you doing today?".format(name))

print(greet(nome))