import random

word_bank = [
    'rizz', 'ohio', 'sigma', 'tiktok', 'skibidi',  
    'apple', 'banana', 'carrot', 'dragon', 'eagle',  
    'falcon', 'galaxy', 'horizon', 'igloo', 'jungle',  
    'kangaroo', 'lantern', 'melody', 'nebula', 'octopus',  
    'penguin', 'quasar', 'rainbow', 'sunrise', 'tornado',  
    'universe', 'volcano', 'waterfall', 'xylophone', 'yacht',  
    'zebra', 'adventure', 'balloon', 'crystal', 'diamond',  
    'elephant', 'fireworks', 'guitar', 'highway', 'island',  
    'jigsaw', 'koala', 'lighthouse', 'mountain', 'necklace',  
    'oasis', 'puzzle', 'quest', 'rocket', 'starfish',  
    'treasure', 'umbrella', 'voyage', 'whirlpool', 'zephyr'
]

word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ')
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
else:
        print('\nYou\'ve run out of attempts! The word was: ' + word)