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
def MathDiscount():
  discount_percentage = (nub_seats/max_seats) * 100
  discounted_flight = discount_percentage * price_flight

  print(discounted_flight)
  again()

#--------------------------------------------------------------------------------

def again(): 
  while yon != 'yes' or yon != 'no':

    yon = input('yes ')

        
    if yon == 'yes': 
      print('hello')
      exit() 
        
    elif yon == 'no': 
      exit()

    else: 
      print(' ')
      print('that is not an opion')
      yon = input(' ')

#--------------------------------------------------------------------------------




#what is this programe 
print("this programe gives you discount depending on how many seats are left on each flight")

#--------------------------------------------------------------------------------


#ask for name
name = input('what is your name : ')

name_len = len(name)
while name_len <= 1 or name_len >= 16:
  if name_len <= 1:
    print('That name is too short')
    name = input('what is your name : ')
    name_len = len(name)
    
  elif name_len >= 16:
    print('That name is too long')
    name = input('what is your name : ')
    name_len = len(name)
    
  else:
    print('')

#--------------------------------------------------------------------------------

#ask what from the dic 
#printing the dic
print("Flight Number", "-","destination/flight")
for key in constants.flight_nub:
  print("     ", key, "      - ",constants.flight_nub[key]['destination'])

#asking what flight are the taking 
print('where do your want to fly to {}?'.format(name))
user_flight  = int(input('plase pick the flight your want to take with the fight number : '))

#--------------------------------------------------------------------------------  

#pulling the numbers from the dic
max_seats = constants.flight_nub[user_flight]['max_nub_of_seats'] 
nub_seats = constants.flight_nub[user_flight]['nub_of_seats_left'] 
price_flight = constants.flight_nub[user_flight]['price'] 

#--------------------------------------------------------------------------------

#asking the use if they can fly tomorrow  
early_bird = input('Are your able to fly tomorrow {}? Yes or No : '.format(name))

while early_bird != "yes" or early_bird != "no":
  if early_bird == "yes": 
    MathDiscount()
      
  elif early_bird == "no": 
    again() 

  else: 
    print(' ')
    print('that is not an opion')
    early_bird = input('Are your able to fly tomorrow {}? Yes or No : '.format(name))
    






#--------------------------------------------------------------------------------
















