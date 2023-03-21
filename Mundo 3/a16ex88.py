import random
for x in range(int(input('Number of games: '))):
    print(f'Game {x+1}: {random.sample(range(1, 60), 6)}')
# i got it from comments. 20/03/23