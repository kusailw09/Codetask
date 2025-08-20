def adventure():
  print("You wake up in a dark forest. Two paths lie ahead.")
  choice1 = input("Do you go left or right?").lower()
  if choice1 == "left":
    print("You meet a friendly frog who helps you escape. You win")
  elif choice1 == "right":
    print("You fall into a trap set by goblins. Game over")
  else:
    print("Invalid choice. The forest swallows you. Game over")

adventure()
