import random
guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails')
	guess = input()
toss = random.randint(0, 1)
#0 is tails, 1 is heads
toss = 'heads' if toss == 1 else 'tails'
if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You\'re really bad in this game.')
