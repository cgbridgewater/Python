# # scambling data

# # def cipher(text, shift, received=False):
# #     SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!,;:()[] '
# #     print(f"SYMBOLS length: {len(SYMBOLS)}")
# #     output = ""
# #     if received:
# #         shift *= -1
# #     for character in text:
# #         print(f'character: {character}')
# #         num = SYMBOLS.find(character.upper())
# #         print(f"num: {num}")
# #         if num + shift >= len(SYMBOLS):
# #             num = num + shift - len(SYMBOLS)
# #         else:
# #             num += shift
# #         if len(output) %2 == 0:
# #             output +- SYMBOLS[num]
# #         else: 
# #             output = SYMBOLS[num] + output
# #             print(f"output flip: {output}")
# #     return output

# # print(f"Output: {cipher('i love soup', 2, True)}")

# def cipher(text, shift, recived=False):
#     SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!,;:()[] '
#     print(f"SYMBOLS length: {len(SYMBOLS)}")
#     output = ""
#     if recived:
#         shift *= -1
#     for character in text:
#         print(f'character: {character}')
#         num = SYMBOLS.find(character.upper()) 
#         print(f"num: {num}")
#         if num + shift >= len(SYMBOLS): 
#             num = num + shift - len(SYMBOLS)
#         else:
#             num += shift
#         if len(output) % 2 == 0:
#             output += SYMBOLS[num]
#             print(f"output not flip: {output}")
#         else:
#             output = SYMBOLS[num] + output
#             print(f"output flip: {output}")
#     return output

# print(f"Output: {cipher('SQCM[GJT[MN', 2)}")







import random

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
