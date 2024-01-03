rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list = ["Rock", "Paper", "Scissor"]
numList = len(list)
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice >= 3 or choice < 0:
  print("You typed an invalid number, you lose!")

else:
  print(list[choice])
  
  computChoice = random.randint(0, numList - 1)
  print("Here is computer choice: ")

  print(list[computChoice])

  
  if choice == 0 and computChoice == 2:
      print("You Win! Rock wins against scissors")
  elif choice == 2 and computChoice == 1:
      print("You Win! Scissors win against paper.")
  elif choice == 1 and computChoice == 0:
      print("You Win! Paper wins against rock.")
  else:
    print("You lose.")
