import random

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice not in range(0,3):
    print("Invalid choice, please try again.")
    
else:
    rock_paper_scissors_list = [rock, paper, scissors]

    print(f"\n{rock_paper_scissors_list[user_choice]}")
    computer_choice = random.randint(0, 2)

    print(f"\nComputer chose:\n\n{rock_paper_scissors_list[computer_choice]}")

    # Draw situation
    if user_choice == computer_choice:
        print("\n\nIt's a draw")
    # Losing situations
    elif (user_choice == 0 and computer_choice == 1) or \
            (user_choice == 1 and computer_choice == 2) or \
            (user_choice == 2 and computer_choice == 0):
        print("\n\nYou lose")
    # Winning conditions
    else:
        print("\n\nYou win!")