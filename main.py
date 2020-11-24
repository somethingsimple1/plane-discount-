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

  CanTheyFly(name, user_flight_nub)

#--------------------------------------------------------------------------------
def CanTheyFly(name, user_flight_nub):

  #asking the use if they can fly tomorrow  
  early_bird = input('Are your able to fly tomorrow {}? Yes or No : '.format(name))

  while early_bird != "yes" or early_bird != "no":
    if early_bird == "yes": 
      MathDiscount(name, user_flight_nub)
        
    elif early_bird == "no": 
      GiveDiscount(name, user_flight_nub) 

    else: 
      print(' ')
      print('that is not an opion')
      early_bird = input('Are your able to fly tomorrow {}? Yes or No : '.format(name))

#--------------------------------------------------------------------------------

def MathDiscount(name, user_flight_nub):
    #pulling the numbers from the dic
  max_seats = constants.flight_nub[user_flight_nub]['max_nub_of_seats'] 
  nub_seats = constants.flight_nub[user_flight_nub]['nub_of_seats_left'] 
  price_flight = constants.flight_nub[user_flight_nub]['price'] 

  seat_number = nub_seats + 1

  discount_percentage = (nub_seats/max_seats) * 100
  price_flight_user = discount_percentage * price_flight


  GiveDiscount(name, user_flight_nub, price_flight_user, seat_number)

#--------------------------------------------------------------------------------

def Adding(name, user_flight_nub):
  nub_seats = constants.flight_nub[user_flight_nub]['nub_of_seats_left'] 
  price_flight = constants.flight_nub[user_flight_nub]['price'] 

  seat_number = nub_seats + 1
  price_flight_user
  GiveDiscount(name, user_flight_nub, price_flight_user, seat_number)

#--------------------------------------------------------------------------------

def GiveDiscount(name, user_flight_nub, price_flight_user, seat_number):
  print(' ')
  print(' ')
  
  print('{}, your flight number is {} and the number seat you have is {}. The price of your flight is going to be ${}'.format(name, user_flight_nub, seat_number, price_flight_user))
  
  print(' ')
  
  again()

#--------------------------------------------------------------------------------

def again():
  yon = 'yon'
  while yon != 'yes' or yon != 'no':

    yon = input('do you want to make anther booking? yes or no? :')

        
    if yon == 'yes': 
      print(' ')
      print(' ')
      print('############################################################')
      print('############################################################')
      print(' ')
      print(' ')
      welcome()

        
    elif yon == 'no': 
      exit()

    else: 
      print(' ')
      print('that is not an opion')
      print(' ')

#--------------------------------------------------------------------------------



welcome()