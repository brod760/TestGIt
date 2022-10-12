"""Write a function that returns the sum of two numbers
for num1 =1 and num2 =2, following output should be =3 """
#def add(num1, num2 ):
    #sum = num1 + num2
    #return sum
"""Floats are numbers that arent intgers. for example 0.5 and -7.8237591
* is use for mult, ** raises it the power of something.
type = input() #if string input desired, then "" needed for the desired target. 
#your code goes here
.append adds to the end of the list.
while loop only does things as long as the conidtion is true
if statement gives you once the possibility to do something or not (something else):
print(len(list)) will print the entire list. 
if type == "Visa" or type == "Amex":
    print("accepted")
True and false
NOT- the result of not True is False, and not false goes to True
for- and operators both need to be true 
for- OR requries one truth, but needs both false to return false
input() stops running the code until it gets user input.
in place operators, the same operators such as -,*,/ and %
Concatenation adds two strings together. print("spam"+"eggs"); output would be spameggs; print("2"+"2"); output 22 
/ is division
// gives you the number on top when you divid. 
\ backslash, used for special characters. 's,or quotes in a string
\n gives you a new line
ex 20 // 6, out would be 3. 6 goes into 20 3 times only
modulo operator % used to get the remainder
BREAK*** Used to break out of the wild loop
FOR LOOPS** - is used to loop when the number of iterations is fixed
WHILE LOOPS** - are used when the number of iterations id not known also depends on some calcualtions and condition in the code block of the loop
FOR VS WHILE** - for loops have shoter syntax, making ut a better choice in most test cases
RANGE - by default it starts from 0, increments by 1 and stops at the selected number range 10 gives numbers from 0-9 0 counts
RETURN - any code after a return will never happen
**Modules**
RANDOM - *import random* module to generate random numbers
MATH - *import math* allows you call functions
EXCEPTIONS - when something goes wrong. causes the program stop
FINALLY - used at the bottom of the try/except, can possibly run after the except block
finally- will run after a divid by zero error
{} - dictionaries - can be nested in a tuple 
[] - lists - can be changed 
() - tuples - similar to list but are immutable (cant be changed)
List slices - another eay of retrieving values from a list [2:6:3] (third number represents the step, causes alternate values in the slice)
List slices - [1:-2] using negative values causes the count to start from the end of the list.
"""




"""Python program for sum the digits of a given number"""
 # example:
 # input: n=11 
 # output: n=2
 # input: n=85
 # output: n=13
"""def getSum(n):
    sum = 0 
    for digit in str(n):
        sum += int(digit)
    return sum
n = 123456789
print(getSum(n))"""

"""Palindrome, given an integer, palindrome reads the same backward as forward"""
# example 121 is a palinrome while 122 isn't
"""import math 
def isPalindrome(n): 
 return str(n) == str(n)[::-1]
n = input() #you can also give n a fixed set of numbers#
print(isPalindrome((n)))"""

"""Python List Reverse()"""
# you are given a list, but you want to return the integers in the list in reverse.
# use the reverse() function to be able to easily return the list.
# using a list of prime numbers.
"""prime_numbers = [2,3,5,7]
prime_numbers.reverse()
#.reverse() method reverses the elements of the list.
print('Reversed List:', prime_numbers)"""

"""Python list of pop()"""
# remove an item at the given index from the list and returns the removed item
#example: programming langues list. # remove the 4th item in the list.
#python index starts at zero not one.
"""lang = ['python','java','c++','ruby','c']
return_value = lang.pop(4)
print('Removed', return_value)
print('new list', lang)"""

"""Python append()"""
#append() adds an item to the end of the list
"""currencies = ['dollar', 'euro', 'pound']
currencies.append('Yen')
print(currencies)"""

"""Python List Count()"""
#using a list, returns the number of times the speified element appears in the list.
"""nums = [2,4,51,63,2,78,2,479,222,3151]
count = nums.count(51)
print(count)"""

print("{0}{1}{0}".format("abra","cad"))