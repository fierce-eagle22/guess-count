number = 9
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess != number and guess != 0:
        print(f'Wrong, {guess_limit - guess_count} more attempt(s) left')
    if guess == number:
        print('You win!')
        break
else:
    print('You lost the game :(')