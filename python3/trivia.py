#!/usr/bin/env python3

class Game:
    def __init__(self): # creates the initial lists that store information
        self.players = []
        self.places = [0] * 6
        self.coins = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.get_out = False

        for i in range(50): # Adds questions to the game 
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self): # you need at least two players to playt the game. This makes sure you have enough players
        return self.how_many_players >= 2

    def add(self, player_name): # This function adds the players and resets all of the other variables to zero
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.coins[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        print(player_name + " was added")
        print("They are player number %s" % self.how_many_players)
        return True
    
    @property
    def count_coins(self): # This is meant to reduce the repition
        return(self.players[self.current_player] + ' now has ' + str(self.coins[self.current_player]) + ' Gold Coins.')

    @property
    def find_location(self): # This is meant to reduce the repition
        return(self.players[self.current_player] + '\'s new location is ' + str(self.places[self.current_player]))
   
    @property # This is meant to reduce the repition
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll): # this function asks the player a question and checks to see if they are in the penalty box
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.get_out = True
                print("%s is getting out of the penalty box" % self.players[self.current_player])
                print(self.find_location)
                print("The category is %s" % self.current_category)
                self.ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.get_out = False

        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 1
            print(self.find_location)
            print("The category is %s" % self.current_category)
            self.ask_question()

    def ask_question(self): # This gives the player a question
        if self.current_category == 'Pop': print(self.pop_questions.pop(0))
        if self.current_category == 'Science': print(self.science_questions.pop(0))
        if self.current_category == 'Sports': print(self.sports_questions.pop(0))
        if self.current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def current_category(self): # this picks a random question to be asked
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def correct(self): # This is checking whether the answer was correct. It then gives coins
        if self.in_penalty_box[self.current_player]:
            if self.get_out:
                print('Answer was correct!')
                self.coins[self.current_player] += 1
                print(self.count_coins)
                winner = self.did_player_win()
                self.current_player += 1
                if self.current_player == self.how_many_players: self.current_player = 0
                return winner
            else:
                self.current_player += 1
                if self.current_player == self.how_many_players: self.current_player = 0
                return True
        else:
            print("Answer was corrent!")
            self.coins[self.current_player] += 1
            print(self.count_coins)

            winner = self.did_player_win()
            self.current_player += 1
            if self.current_player == self.how_many_players: self.current_player = 0

            return winner

    def wrong(self): # this sends the player to the penalty box if they answered the question wrong
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == self.how_many_players: self.current_player = 0
        return True

    def did_player_win(self): # this checks if the player won
        return not (self.coins[self.current_player] == 6)


from random import randrange #, seed

if __name__ == '__main__': # running the code above 
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    # seed(3)

    while True:
        game.roll(randrange(5) + 1)
        if randrange(9) == 7:
            not_a_winner = game.wrong()
        else:
            not_a_winner = game.correct()
        if not not_a_winner: break