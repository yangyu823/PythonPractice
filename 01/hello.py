import random
import sys
import os

print("Hello world")
'''
Mulitilineafhsdjvkhakd
'''

name='Derek'
print(name)

# Number

print("5 + 2 = ",5+2)
print("5 - 2 = ",5-2)
print("5 * 2 = ",5*2)
print("5 / 2 = ",5/2)
print("5 % 2 = ",5%2)
print("5 ** 2 = ",5**2)
print("5 // 2 = ",5//2)

# String

quote ="\" Always remember you are unique"

multi_line_quote = ''' Just
like everyone else'''

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print('\n' * 5)

print("I dont like ", end="")
print("newlines")


# Lists
grocery_list = ['Juice' , 'Tomatoes' , 'Potatoes',
                 'Bananas']

print('First Item', grocery_list[0])

grocery_list[0] ="Green Juice"

print('First Item', grocery_list[0])

other_events =['Wash Car' , 'Pick Up kids', 'Cash Check']

to_do_list = [other_events,grocery_list]

print(to_do_list)

print(to_do_list[1][1])

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(3,'bapple')
print(to_do_list)

grocery_list.remove('bapple')
grocery_list.sort()
grocery_list.reverse()
print(to_do_list)

del grocery_list[4]
print(to_do_list)

to_do_list2=other_events+grocery_list
print(to_do_list2)

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))


# Tuples
pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list= tuple(new_tuple)

#print(type(new_tuple))

print(len(new_tuple))
print(min(new_list))
print(max(new_tuple))

# Dictionaries


super_bike ={'ducati' : 'panigale 1299',
             'kawasaki' : 'ninja H2',
             'yamaha' : 'r1m',
             'honda' : 'cbr1000rr',
             'suzuki' : 'gsx-1000'}

print(super_bike['ducati'])

del super_bike['suzuki']

print(super_bike.keys())

print(super_bike.values())