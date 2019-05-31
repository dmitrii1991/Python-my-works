from Picture import human
words = ['robot', 'stone', 'axe', 'sword', 'flower']

class Hangman:

    def __init__(self, base_words):
        self.base_words = base_words

    def programm(self):

        def choiсe(self): #  RANDOM choiсe word and remove from list
            import random
            choiсe_word = random.choice(self.base_words)
            self.base_words.remove(choiсe_word)
            return choiсe_word


        def stat_word (word): #  the account of the state of the word
            basa = {}
            i = 0
            for letter in list(word):
                basa[i] = {"let": letter, "stat": "unknown"}
                i += 1
            return basa

        word = choiсe(self)
        stat_word = stat_word(word)

        letter_player = ''
        victory = False
        life = 8
        wrong_letters = set()

        while victory == False:
            print(human[8-life])
            print("guess the word: ", end='')
            i = end_game  = 0

            for letter in list(word):
                if letter_player == stat_word[i]["let"]:  # check for availability
                    stat_word[i]["stat"] = "known"

                if stat_word[i]["stat"] == "unknown":  # status output
                    print("_ ", end='')
                    i += 1
                else:
                    print(letter, end='')
                    i += 1
                    end_game += 1

            if wrong_letters != set():
                print('\nWrong letters:', wrong_letters)  # output incorrect answers
            letter_player = input("\nEnter letter:\n")  # enter the letters from the player

            if letter_player not in list(word):  # checking the correctness of the player's letter
                if len(letter_player) != 1:
                    print("ENTER 1 LETTER! ")
                elif letter_player in wrong_letters:
                    print("ENTER AGAIN WRONG VARIANT! ")
                elif letter_player in list('1234567890-_=+|\/?>.<,~`!@#$%^&*()]}{["'):
                    print("NOT LETTER")
                else:
                    wrong_letters.add(letter_player)
                    life -= 1

            if end_game == len(word)-1: # check at the end of the game
                victory = True
                print("YOU WIN!!!!")
            elif life == 0:
                print("YOU LOST!!!!")
                print(human[8])
                victory = None
            else:
                print("_________NEXT MOVE_________")

if __name__ == "__main__":
    Hangman(words).programm()
