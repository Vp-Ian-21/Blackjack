from blackjack_helper import *

players_num = int(input("Welcome to Blackjack! How many players? "))
players = []
scores = {}

for i in range(players_num):
  name = input(f"What is player {i+1}'s name? ")
  players.append(name)
  scores[name] = 3      # Each player starts with a score of 3

while players:  # Continue while there are players left
  hands = {}  # Store the hand value for each player to avoid overwriting the value.
  
  # USER'S TURN
  for player in players:
    user_hand = draw_starting_hand(player + "'S")
    while user_hand < 21:
      should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
      if should_hit == 'n':
        break
      elif should_hit != 'y':
        print("Sorry I didn't get that.")
      else:
        user_hand += draw_card()
    print_end_turn_status(user_hand)
    hands[player] = user_hand
    
  # DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand += draw_card()
  print_end_turn_status(dealer_hand)
  print_header('GAME RESULT')

  # Check results for each player after both the user and dealer have finished their turns
  for player in players[:]:
    if hands[player] <= 21 and (hands[player] > dealer_hand or dealer_hand > 21):
      # Player wins
      scores[player] += 1
      print(f"{player} wins! Score: {scores[player]}")
    elif hands[player] > 21 or (dealer_hand <= 21 and dealer_hand > hands[player]):
      # Player loses
      scores[player] -= 1
      print(f"{player} loses! Score: {scores[player]}")
    else:
      # Player pushes (tie)
      print(f"{player} pushes. Score: {scores[player]}")
        
    # In order to eliminate a player, when their score reaches 0, they are removed.
    if scores[player] <= 0:
      print(f"{player} eliminated!")
      players.remove(player)

  # If all the players are eliminated.
  if not players:
    print("All players eliminated!")
    break

  # Ask if players want to play again.
  rematch = input("Do you want to play another hand (y/n)? ")
  if rematch == 'n':
    break


