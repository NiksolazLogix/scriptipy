import emoji
import random

# 0 = paper
# 1 = stone
# 2 = scissor

def game():
  print('''
  0 = paper
  1 = stone
  2 = scissor
  ''')
  player = int(input('Insert your choice: '))
  computer = random.randint(0, 2)
  if player == computer:
    print('Draw \U0001F610')
  elif player == 0 and computer == 1:
    print('You win! \U0001f600')
  elif player == 0 and computer == 2:
    print('You lose! \U0001F636')
  elif player == 1 and computer == 0:
    print('You lose! \U0001F636')
  elif player == 1 and computer == 2:
    print('You win! \U0001f600')
  elif player == 2 and computer == 0:
    print('You win! \U0001f600')
  elif player == 2 and computer == 1:
    print('You lose! \U0001F636')
  else:
    print('Invalid option')

game()