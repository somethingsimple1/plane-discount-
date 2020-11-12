import math 
import constants
"""
what is this program going to do 

1.	WAIKATO AIR is based in Hamilton and flies to 3 regular destinations, Auckland, Wellington and Rotorua.

2.	Each day they send an email to their customers with details of their discount fares (‘discount fare’, ‘percentage discount’ and ‘discount type’) for people who can fly the next day. The details of the discounts vary each day depending on how many seats are left on each flight.

3.	WAIKATO AIR needs a program that will produce text detailing these discounts that WAIKATO AIR can then copy into a bulk email that they will send to all their members (you are only required to produce the text for WAIKATO AIR to copy. You do not produce the actual email).


NOTES: 


Equation: P% * X = Y or P% = (Y/X) * 100


amount of seats left : (input by user)
the destinations : Auckland, Wellington and Rotorua


percentage discount : the percentage discount 
discount fare : toatal discount 
discount type : 

"""

#what is this programe 
print("this programe gives you discount depending on how many seats are left on each flight")

#--------------------------------------------------------------------------------

#ask for name
name = input("what is your name : ")
name_len = len(name)
#
while name_len <= 1 or name_len >= 16:
  if name_len <= 1:
    print('That name is too short')
    name = input("what is your name : ")
    name_len = len(name)
  
  elif name_len >= 16:
    print('That name is too long')
    name = input("what is your name : ")
    name_len = len(name)
  
  else:
    s
  
    
#--------------------------------------------------------------------------------

#ask what from the dic 
# printing the dic
for key in constants.flight_nub:
  print(key, constants.flight_nub[key]['destination'])

#--------------------------------------------------------------------------------  

#asking what flight are the taking 
print('where do your want to fly to {}?'.format(name))
user_flight  = input('plase pick the flight your want to take with the fight number : ')

#--------------------------------------------------------------------------------
#math for the discount 



#--------------------------------------------------------------------------------

def early_bird():
  #asking the use if they can fly tomorrow  
  early_bird = input('Are your able to fly tomorrow {}? Yes or No : '.format(name))
  if early_bird == "yes": 
    print(" ")
    
  elif early_bird == "no": 
    print(" ")

  else: 
    print('that is not an opion')












