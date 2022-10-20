import random

tries = 8
previous_guesses = []
games_played = 0
win = 0
new_guess = True

while new_guess == True:
  number = random.randint(0,100)
  #print(number) #debug
  new_guess = False
  

while tries >= 1 and new_guess == False:
  guess = int(input("Guess a number from 0 to 100: "))
  previous_guesses.append(guess)
  games_played = + 1

  if  guess < number:
    print("Your guess is low, try again")

  elif guess > number:
    print("Your guess is high, try again")
  
  print("")
  
  
  if guess == number:
    print("Congrats, your guess is right")
    win = + 1
    previous_guesses.remove(guess)
    new_guess = True
    
      
  else:
    tries = tries - 1
    print("")
    print(f"your previous guesses: {previous_guesses}")
  
  if tries == 0:
    print("No more chances!")
    print(f"Games played: {games_played}")
    print(f"games won: {win}")

  elif guess == number:
    print(f"Games played: {games_played}")
    print(f"games won: {win}")
  
  if previous_guesses == guess:
    print("You guessed that number already!")
    print("Your previous guesses were:")
    print(previous_guesses)