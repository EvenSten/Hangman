import randomGameWord

lives = 6
dead = ""
text = randomGameWord.gameWord
count = text.lower().count('o')
guess = " "
total = 0
neededAmount = len(randomGameWord.gameWord)
rightLetters = []
wrongLetters = []



print("Welcome to Hangman. You will have 5 lives to guess all the letters in the word. If all five lives are used, then you lose the game.")
print()
for i in range(len(randomGameWord.gameWord)):
        print("_ ", end=" ")
while dead != "True":
    print()
    guess = input("Guess a letter: ")
    count = text.lower().count(guess.lower())
    if count > 0 and guess not in rightLetters:
          print("Great ", guess, " was there!")
          total = total + count
          rightLetters.append(guess)
          print("You have already guessed: ", rightLetters)
          if total == neededAmount:
                print("You got it the word was ", randomGameWord.gameWord)
                dead = "True"
    elif count > 0 and guess in rightLetters:
          print("Already guessed that try again")
          print("You have already guessed: ", rightLetters)
    elif count <= 0 and guess not in wrongLetters:
          print("Not Good", guess ,"wasn't there")
          lives = lives - 1
          wrongLetters.append(guess)
          print("Remaining Lives: ", lives)
          print("You have already guessed: ", wrongLetters)
          if lives == 0:
                print("Too bad you lost, the word was ", randomGameWord.gameWord)
                dead = "True"
    else:
          print("Still wrong")
          print("You have already guessed: ", wrongLetters)
    

print("The game is over.")

print(randomGameWord.gameWord)


