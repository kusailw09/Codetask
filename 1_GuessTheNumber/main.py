import random
print("Welcome to guess the number game")
number = random.randint(1, 100)
guess = None
while guess != number:
  guess = int(input("Guess a number between 1 and 100: "))
  if guess < number:
    print("Too low")
  elif guess > number:
    print("Too high")
  else:
    print("Congratulations! you guessed it right")
