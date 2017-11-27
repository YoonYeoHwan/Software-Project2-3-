from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter : ')

        # 알파벳 이외의 입력 예외처리
        if guessedChar.isalpha() != True:
            print('You have to input an alphabet.')
            continue
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue


        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('word [' + guess.secretWord + ']')
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':

    menu = 0

    while menu == 0:
        print("*" * 27)
        print("*** LET'S START HANGMAN ***")
        print("*" * 27)
        gameMain()
        menu = int(input("RESTART : 0, EXIT : 1\n"))

        if menu == 0:
            continue
        else:
            print("GAME OVER")
