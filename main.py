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

"""


def welcome(): 
  #what is this programe 
  print('this programe gives you discount depending on how many seats are left on each flight')

  #ask for name


  name_len = -1
  while name_len <= 1 or name_len >= 16:

    name = input('what is your name : ')
    name_len = len(name)

    if name_len <= 1:
      print('That name is too short')
    
    elif name_len >= 16:
      print('That name is too long')
      
    else:
      print(' ')
      print('==============================')
      print(' ')
      flying(name)


#--------------------------------------------------------------------------------

def flying(name):
  name = name

  print("Flight Number", "-"," destination/flight")

  for key in constants.flight_nub:
    print("     ", key, "      - ",constants.flight_nub[key]['destination'])

  print(' ')
  print('==============================')
  print(' ')

  #asking what flight are the taking 
  print('where do your want to fly to {}?'.format(name))
  user_flight_nub  = int(input('plase pick the flight your want to take with the fight number : '))

  



welcome()