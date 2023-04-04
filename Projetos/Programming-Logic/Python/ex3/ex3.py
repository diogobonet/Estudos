'''
We need a function that can transform a number (integer) into a string.
What ways of achieving this do you know?
Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
'''

numero = int(input("Type a number: "))

def number_to_string(num):
    string = str(num)
    string2 = ("'{}'".format(string))
    return string2

print(number_to_string(numero))