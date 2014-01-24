# Guessing Game Revised

# Imports
import random

# Create a word list
WORDS = ('sculpture', \
         'collapse', \
         'economy', \
         'president', \
         'weakness', \
         'unemployment'
         )

# Pick a random word from the list
scores = []
choice = None

# Create Menu
print("""

        Welcome to the word guessing game
        You get 10 tries to guess a letter
        Guesses cost points:
           Letters:            Words:
        cost 10 points     cost 20 points
     """
      )
while choice != '0':
    pScore = 160
    print("""
       0 - Exit
       1 - New Game
       2 - Top Score's
       """)
    choice = input('Please choose an option (0-2): ')
    if choice == '0':
        print('Thanks for playing')
    elif choice == '1':
        word = random.choice(WORDS)
        used = []
        pLetters = '-' * len(word)
        uName = input('\nPlease enter your name: ')
        pGuess = None
        pLetter = None
        choose = None
        count = 0
        # Have player guess the word
        while pGuess != word and pScore >= 0 and choose != '3':
            print('\nYou\'ve used the following letters:' \
                   + '\n', used, '\nSo far, the word is:\n', pLetters)
            print("""
        1 - Guess a letter
        2 - Guess the word
        3 - Give up
        """)
            print('You have guessed', count, 'out of 10 letters')
            choose = input('Please make a choice (1-3): ')
            if choose == '1' and count < 10 and pScore > 0 and choose != '':
                print('\nYou\'ve used the following letters:' \
                      + '\n', used, '\nSo far, the word is:\n', pLetters)
                pLetter = input('What letter would you like to guess? ')
                pLetter = pLetter.lower()
                used.append(pLetter)
                if pLetter in word:
                    print('Congradulation\'s', pLetter.upper(), 'was found in the word')
                    new = ''
                    for x in range(len(word)):
                        if pLetter == word[x]:
                            new += pLetter
                        else:
                            new += pLetters[x]
                    pLetters = new
                    count += 1
                else:
                    count += 1
                    pScore -= 10
            elif choose == '1' and count == 10:
                print('Sorry but you ran out of letter guesses')
            elif choose == '2' and pScore > 0:
                print('\nYou\'ve used the following letters:' \
                      + '\n', used, '\nSo far, the word is:\n', pLetters)
                pGuess = input('What do you think the word is? ')
                if pGuess in word and pScore >= 20:
                    print('That is correct, the word', pGuess, 'is the correct word!')
                    entry = (str(pScore), uName)
                    scores.append(entry)# Add the user's score and name
                    scores.sort(reverse=True)   # Sort the scores in Decending
                    scores = scores[:5]         # Keep only the top 5 scores
                elif pGuess != word and pScore >= 20:
                    print('Sorry but', pGuess, 'is not the correct word')
                    pScore -= 20
                else:
                    print('Sorry but you don\'t have enough points to guess the word.')
                    print('Your score was,', pScore)
            elif choose == '3':
                print('\nYou SUCK!!')
            else:
                print('\nSorry but I didn\'t recognize your command')
    elif choice == '2':
        x = 0
        print('Score : Name')
        while x < len(scores):
            print(' : '.join(scores[x]))
            x += 1

input('\n\nPress the enter key to exit.')
