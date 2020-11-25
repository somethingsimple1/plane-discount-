import sys
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

#--------------------------------------------------------------------------------
def welcome(): 
  #telling the  users what the programe is  
  print('this programe gives you discount depending on how many seats are left on each flight')
  print(' ')
  print(' ')
  print(' ')

  

  #this is to ask for the users name and to test the lenth of the user name to make it fit 
  name_len = -1
  while name_len <= 1 or name_len >= 16:

    print('what should we call you?')
    print('(all spaces will be removed)')
    name = str(input('You can only 2 - 16 characters. : '))
    name_len = len(name)
    name = name.replace(" ", "")


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

#printing and asking the user for what flight they want to take 
def flying(name):
  name = name

  #printing out the list of flights 
  print("Flight Number", "-"," destination/flight")

  for key in constants.flight_nub:
    print("     ", key, "      - ",constants.flight_nub[key]['destination'])

  print(' ')
  print('==============================')
  print(' ')

  
  user_flight_nub = -99
  while  constants.flight_nub.get(user_flight_nub) is None:
    try:
      #asking what flight the user wants 
      print('where do your want to fly to {}?'.format(name))
      user_flight_nub  = int(input('plase pick the flight your want to take with the fight number : '))
      

      if constants.flight_nub.get(user_flight_nub) is None:
        print('that is not a flight number')
      

      else:
        CanTheyFly(name, user_flight_nub)

    except ValueError:
      print('that is not a flight number')

  
#--------------------------------------------------------------------------------
#asking if they can fly tomorrow 
def CanTheyFly(name, user_flight_nub):

  
 
  early_bird ='yon'
  #yes or no? code
  while early_bird != "yes" or early_bird != "no":

    #asking the use if they can fly tomorrow  
    early_bird = str(input('Are your able to fly tomorrow {}? Yes or No : '.format(name)))
    early_bird = early_bird.replace(" ", "")
    early_bird = early_bird.lower()

    if early_bird == "yes": 
      MathDiscount(name, user_flight_nub)
        
    elif early_bird == "no": 
      Adding(name, user_flight_nub) 

    else: 
      print(' ')
      print('that is not an opion')

#--------------------------------------------------------------------------------

#the math for the discount if they are going to fly the next day 
def MathDiscount(name, user_flight_nub):
  #pulling the numbers from the dic
  max_seats = constants.flight_nub[user_flight_nub]['max_nub_of_seats'] 
  nub_seats = constants.flight_nub[user_flight_nub]['nub_of_seats_left'] 
  constants.flight_nub[user_flight_nub]['nub_of_seats_left']  += 1 #adding 1 to the amout of seats left
  price_flight = constants.flight_nub[user_flight_nub]['price'] 

  tomorrow_flying = "True" #

  #adding 1 to the seats so that the user can see what number seat they have
  seat_number = nub_seats + 1

  #math--
  discount_percentage = (nub_seats/max_seats) * 100

  p = discount_percentage * price_flight / 100

  price_flight_user = price_flight - p

  GiveDiscount(name, user_flight_nub, price_flight_user, seat_number, tomorrow_flying)

#--------------------------------------------------------------------------------
#this is if the user can fly the next day
def Adding(name, user_flight_nub):
  #pulling the numbers from the dic
  nub_seats = constants.flight_nub[user_flight_nub]['nub_of_seats_left'] 
  constants.flight_nub[user_flight_nub]['nub_of_seats_left']  += 1 #adding 1 to the amout of seats left
  price_flight = constants.flight_nub[user_flight_nub]['price'] 

  tomorrow_flying = "False"

  #math--
  seat_number = nub_seats + 1
  price_flight_user = price_flight
  GiveDiscount(name, user_flight_nub, price_flight_user, seat_number, tomorrow_flying)

#--------------------------------------------------------------------------------

#giving the user the what there flight number is, the price of the fight, and what number seat they have
def GiveDiscount(name, user_flight_nub, price_flight_user, seat_number, tomorrow_flying):
  print(' ')
  print(' ')
  
  print('{}, your flight number is {} and the number seat you have is {}. The price of your flight is going to be ${}'.format(name, user_flight_nub, seat_number, price_flight_user))
  
  print(' ')

  d = {}
  #adding everying to a user dic 
  d['user_flight_nub'] = user_flight_nub
  d['seat_number'] = seat_number
  d['price_flight_user'] = price_flight_user
  d['tomorrow_flying'] = tomorrow_flying
  constants.user[name] = d
  



  
  again()

#--------------------------------------------------------------------------------

#asking if they want to make anther booking 
def again():
  yon = 'yon'
  while yon != 'yes' or yon != 'exit':

    #asking
    yon = input('do you want to make anther booking? yes or exit? :')
    yon = yon.replace(" ", "")
    yon = yon.lower()

    #if yes
    if yon == 'yes': 
      print(' ')
      print(' ')

      print('############################################################')
      print('############################################################')
      print(' ')
      print(' ')
      welcome()

    #if exit
    elif yon == 'exit': 
      for i in range(1,5):
        i += i
        print('----------')

      print('here is all the users')
      print(constants.user)

      for i in range(1,5):
        i += i
        print('----------')

      print("This programe has been terminated")
      exit()
      

    else: 
      print(' ')
      print('that is not an opion')
      print(' ')

#--------------------------------------------------------------------------------



welcome()



 