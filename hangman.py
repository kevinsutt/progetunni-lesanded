import random
k = 0
print("Hangman")
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda weasel whale wolf wombat zebra'.split())
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  O   |
      |
      |
     ===''','''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

def getrandomword(wordlist):
    randomword = random.randint(0, len(words) - 1 )
    return wordlist[randomword]

def display(missedletters, correctletters, secretword):
    if k < 6:
        print(HANGMAN_PICS[len(missedletters)])
    print()
    
    print('Missed letters:', end=' ')
    for letter in missedletters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(secretword)
    
    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks[:1] + secretword[i] + blanks[i+1:]
        
    print()
    
def getguess(alreadyguessed):
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyguessed:
            print("You have already guessed that letter. Choose again please.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter only a letter!")
        else:
            return guess

secretword = getrandomword(words)
missedletters = ''
correctletters = ''
failurecount = len(secretword)
gameisdone = False

while True:
    display(missedletters, correctletters, secretword)
    guess = getguess(missedletters + correctletters)
    if guess in secretword:
        correctletters = correctletters + guess
        foundallletters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                foundallletters = False
                break
        if foundallletters:
            print("Correct, the secret word is " + str(secretword))
            gameisdone = True
    else:
        k = k + 1
        missedletters = missedletters + guess
        if len(missedletters) == len(HANGMAN_PICS) - 1:
            display(missedletters, correctletters, secretword)
            print("You have run out of guesses! Loser!")
            print("Word was " + str(secretword))
            gameisdone = True
            break
 
 








