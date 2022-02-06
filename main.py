#import data from game_data
#import logo from art

from art import logo, vs
from game_data import data
from random import randint
import replit


#choose two random integer within range of 1 to 50
option_a= randint(0, 50)
option_b= randint(0, 50)
if option_a== option_b:
  option_b= randint(0, 50)
# print (option_a)
# print (option_b)
def clear_and_display_logo():
  """clear screen and print Game name logo"""
  replit.clear()
  print(logo)

def display_item(item):
    return(data[item]['name'], data[item]['description'],data[item]['country'], data[item]['follower_count'])

def display_accounts(item_a, item_b):
    #print 'A', choose a random entry and assign it to A.
    # print (item_a)
    print (f"Compare A: {item_a[0]}, a {item_a[1]}, from {item_a[2]}")
    #print VS logo
    print(vs)
    #print 'B', choose a random entry and assign it to B.
    print (f"Against B: {item_b[0]}, a {item_b[1]}, from {item_b[2]}")


#compare A and B based on follower count. If answer is correct, increase the score by 1, and replace A with B entry and choose a new entry for B.
def compare_item(item_a, item_b):
  if( item_a[3] > item_b[3]):
    winner = 'a'
  elif(item_a[3] < item_b[3]):
    winner = 'b'
  else:
    winner = 'b'
  return winner


def take_a_guess():
    guess =(input("Who has more followeres? Type 'A' or 'B'?: ")).lower()
    return guess

# def swap_item(item_a, item_b):
#       item_a=item_b
#       item_b= display_item(randint(0,50))
#       return item_a, item_b


score=0
#take input from User between A & B.
def game():
  clear_and_display_logo()
  game_over = False

  #print 'A', choose a random entry and assign it to A.
  item_a= display_item(option_a)
  item_b= display_item(option_b)
  display_accounts(item_a, item_b)
  while game_over== False:


    winner= compare_item(item_a, item_b)

    # print (winner)
    global score

    guess= take_a_guess()
    if (guess == winner):
      score += 1
      item_a=item_b
      item_b= display_item(randint(0,50))
      while item_a == item_b:
        item_b = display_item(randint(0,50))
      print(f" after a guess: {item_b}")
      clear_and_display_logo()
      print (f"You're right, current score: {score}")
      display_accounts(item_a, item_b)
      # return game_continues.
    else:
      game_over= True
  clear_and_display_logo()
  print (f"Sorry, that's wrong, Final score: {score}")

#if answer is incorrect, end the game and print the score of user so far. 

game()