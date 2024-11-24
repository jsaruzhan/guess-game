import random 

wordlist = ['apple', 'car', 'dog', 'elephant', 'mango', 'dates', 'school', 'weather', 'bed', 'house']

word = random.choice(wordlist)
n = 0
letters = []
g_w = ['_'] * len(word)

def guessWord():
    print("Guess the word based on the blanks: ", ' '.join(g_w))


print("Welcome to the guessing the word game")
guessWord()

while n < 5:
    l = input("Guess one of the letters: ").lower()
    if l in letters:
        print("You have already guest it. Try again")
        guessWord()
    else:
        letters.append(l)
        if l in word:
            for i in range(len(word)):
                if l == word[i]:
                    g_w[i] = l
            print("Good job the word has letter", l, ".Now: ", ' '.join(g_w))
        else:
            n += 1
            print(f"The word does not have letter: {l} in it. Try again, you have {5 - n} guesses left")
            guessWord()
    if ''.join(g_w) == word:
        print("Congrats, You won!")
        break

if n == 5:
        print("You lost :( The word was: ", word)