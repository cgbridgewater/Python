
possible_phrases = ['cat', 'dog', 'computer', 'president', 'introduction', 'dictionary', 'practice', 'racing', 'introduction', 'spelling']


def hangman(word):
    board = set_board(word)
    guesses = 6
    while board != word and guesses > 0:
        print(f'{board} : You have {guesses} guesses left.')
        guess = input('Choose a letter ')
        correct_guess = False
        for index in range(len(word)):
            if guess.lower() == word[index].lower():
                board = board[:index] + word[index] + board[index+1:]
                correct_guess = True
        if not correct_guess : guesses -= 1
    if guesses: print(f'---YOU WIN--- The word was "{word}"')
    else: print(f'---YOU LOSE!!--- Try to be smarter next time, The word was "{word}"')


def set_board(word):
    board = ''
    for letter in word:
        if letter == ' ' : board +=' '
        else: board += '#'
    return board


while input('Do you want to play a game? Y/N   -->  ').lower()== 'y':
    hangman(possible_phrases[random.randrange(len(possible_phrases))])
