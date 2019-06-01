from for_field_of_miracles import *
import random
import time

class Game:

    def __init__(self, base_words: list, players: list):
        self.base_words = base_words
        self.player = input('Print your name (10 letters)\n')
        self.players = players
        self.score = [0, 0, 0]
        self.use_letters = set()
        self.set_of_words = list(LETTERS)


    def game_choice(self):
        self.word = random.choice(self.base_words)  # choice word for game
        self.base_words.remove(self.word)  # delete word from list
        self.players = random.sample(self.players, 2)  # choice enemy
        self.players.append(self.player)  # list of players
        self.safe = {}  # status letters of WORD
        i = 0
        for letter in list(self.word['key']):
            self.safe[i] = {'let': letter, 'stat': 'unknown'}
            i += 1
        self.len = i  # WORD length


    def game_status(self):
        # Game.game_choice(self)
        print('\n', self.word['def'], '\n\n', 'WORD:', end='')
        i = 0
        self.victory = True
        for letter in list(self.word['key']):
            if self.safe[i]['stat'] != 'unknown':
                print(letter, ' ', end='')
                i += 1
            else:
                self.victory = False
                print('_ ', end='')
                i += 1

        if self.use_letters != set():
            print('\n Used letters: ', self.use_letters)

        print('\n', '_'*34)
        print("|{:^10}|{:^10}|{:^10}|".format(self.players[0], self.players[1], self.players[2]))
        print('|' + '-' * 10 + '|' + '-' * 10 + '|' + '-' * 10 + '|')
        print("|{:^10}|{:^10}|{:^10}|".format(self.score[0], self.score[1], self.score[2]))
        print('|' + '_' * 10 + '|' + '_' * 10 + '|' + '_' * 10 + '|')
        print('\n')


    def first_game(self):
        Game.game_choice(self)
        Game.game_status(self)
        game = True
        while game == True:  # status game
            for i in range(0, 3, 1):  # the moves of players
                move_player = True

                while move_player == True:
                    move_player = False

                    if self.players[i] != self.player:  # the choice of the opponent
                        try:
                            self.answer = random.choice(self.set_of_words)
                            self.set_of_words.remove(self.answer)
                        except:
                            pass
                    else:
                        status_letter = False  # check the input of the player
                        while status_letter == False:
                            self.answer = input('Enter your letter \n')
                            if len(self.answer) >= 2:
                                print('ENTER 1 LETTER')
                            elif self.answer in list('1234567890!@#$%^&()_+=-/.,<>?|\\`~'):
                                print('ThIS is not LETTER!')
                            elif self.answer in self.use_letters:
                                print('ThIS LETTER has been')
                            else:
                                self.set_of_words.remove(self.answer)
                                status_letter = True

                    print('PLAYER: {} SAYS LETTER: {}'.format(self.players[i], self.answer))
                    time.sleep(3)

                    for x in range(self.len):  # check for a match
                        if self.safe[x]['let'] == self.answer and self.safe[x]['stat'] == 'unknown':
                            self.safe[x]['stat'] = 'known'
                            move_player = True
                            point = random.randint(1, 10) * 100
                            self.score[i] += point
                            print('Jakubowicz:Congratulations! The letter {} is in the word! Open the letter {}! You '
                                  'have {} points! Even curumim Drum'.format(self.answer, self.answer, point))
                            time.sleep(3)
                        else:
                            self.use_letters.add(self.answer)
                    time.sleep(3)
                    Game.game_status(self)

                    if self.victory == True:
                        game = False
                        print('VICTORY!!!! {} get{} points!'.format(self.players[i], self.score[i]))
if __name__ == "__main__":
    Game(WORD, PLAYERS).first_game()
