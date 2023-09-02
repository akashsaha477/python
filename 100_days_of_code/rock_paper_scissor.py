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

x=[rock,paper,scissors]
z=random.randint(0,2)
print(f"Computer chose:{x[z]}")
y=int(input("Rock=0 , Paper=1 , Scissors=2\n"))
if(y>=3 or y<0):
    print("invalid input")
else:
    print(f"You chose {x[y]}")
    if y== 0 and z== 2:
        print("You win!")
    elif z == 0 and y == 2:
        print("You lose")
    elif z > y:
        print("You lose")
    elif y > z:
        print("You win!")
    elif z == y:
        print("It's a draw")