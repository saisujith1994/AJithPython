# How to convert a number into a string?
from logging import exception
from operator import concat

num= 7
print(f"Converted {num} of type :{type(num)} into a string , type:{type(str(num))}")
# How to join two strings? What happens when an integer and string is tried to join?
print("Joining two strings:")
word= 'Honey bunny '
print(f"word:{word}, \n\tnow ater concatinating \nusing + :{word+' reddy'}\nusing concat: {concat(word," reddy")}")
try:
    print(7+"ballayya")
    #print(2/0)
except Exception as e:
        print((e))
# What function can be used to add a string after each character in a string?(Hint: join)
print("XXX".join("Reddy"))
# What are the functionality of lower, upper, strip, capitalize?
print(f"Lower:{word.lower()}\tUpper:{word.upper()}\tcapitalize:{word.capitalize()}\ttitle:{word.title()}\nlength before strip:{len(word)} after strip {len(word.strip())}:{word.strip()}")

# What do you mean by indexing? How to reverse a string?
print(f"word:{word[:]}, reverse word:{word[::-1]}")
# Are strings mutable? If yes then change the value of the string (sit - - - Fit)
try:
    word[0]='d'
except Exception as e:
    print(e)
# What is text formatting?
print(f"word:{word[:-2]},number:{22/7:.3f}")
# Difference between a sub() function and in operator?
# Explain rstrip, lstrip,
