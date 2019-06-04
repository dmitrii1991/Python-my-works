from hangman import HUMAN
import time
WORDS = ['robot', 'stone', 'axe', 'sword', 'flower', 'week']


def intro():
    print("Colambia \"NeDoPicture\" presets.......")
    time.sleep(1)
    print('H A N G M A N Ver-1.6')
    time.sleep(1)


def choiсe_word(words: list):  # RANDOM choiсe word, remove from list and get status for letters in word
    import random
    choiсe_word = random.choice(words)
    words.remove(choiсe_word)

    status_letters_in_word = {}
    i = 0
    for letter in list(choiсe_word):  # Getting status for each letter
        status_letters_in_word[i] = {"let": letter, "stat": "unknown"}
        i += 1
    return choiсe_word, status_letters_in_word, words


def display_board(used_letters: set, status_letters_in_word: dict, lifes: int, stat_human: list):  # output image&status
    print(stat_human[len(stat_human) - lifes])
    if used_letters != set():
        print('Used letters: ', used_letters)
    else:
        print('Used letters: ')

    for i in status_letters_in_word:
        if status_letters_in_word[i]["stat"] != "unknown":
            print(status_letters_in_word[i]['let'], ' ', end='')
            i += 1
        else:
            print('_ ', end='')
            i += 1
    print('\n')

if __name__ == "__main__":
    play_game = True
    intro()
    while play_game == True:  #
        choiсe_word1, status_letters_in_word, WORDS = choiсe_word(WORDS)
        lifes = 9
        one_game = True
        used_letters = set()

        while one_game == True:
            display_board(used_letters, status_letters_in_word, lifes, HUMAN)
            player_letter = input('Enter letter\n')
            check_player_letter = False
            if len(player_letter) == 1 and (player_letter not in used_letters) and (player_letter not in list(' 1234567890-=!@#$%^&*()_+/.,<>?;:')):
                used_letters.add(player_letter)
                for i in range(len(choiсe_word1)):
                    if status_letters_in_word[i]['let'] == player_letter:
                        status_letters_in_word[i]['stat'] = 'known'
                        check_player_letter = True

                if check_player_letter != True:
                    lifes -= 1
                    print("wrong answer!")
                    time.sleep(1)
                else:
                    print("FINE!")
                    one_game == False
                print('---------Next---------')
            elif len(player_letter) != 1:
                print("Length must be 1 !")
            elif player_letter in list(' 1234567890-=!@#$%^&*()_+/.,<>?;:'):
                print("Not LETTER!")
            elif player_letter in used_letters:
                print("LETTER is USED!")

            one_game = False
            for i in range(len(choiсe_word1)):  # check on victory
                if status_letters_in_word[i]['stat'] != 'known':
                    one_game = True

            if one_game == False:
                print('YEPPPP YOU WIN!!')
            elif lifes == 1:
                print('OYYYYYY YOU DIE!!')
                print(HUMAN[8])
                one_game = False

        play_again = input('press 1 to exit\n')
        if play_again == "1":
            play_game = False
