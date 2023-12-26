class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.current_player = 'X'

    def print_board(self):
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print('-+-+-')
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print('-+-+-')
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print('This position is already taken. Choose another one.')

    def check_win(self):
        win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6))
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board

    def play_game(self):
        print('Welcome to Tic Tac Toe!')
        print('Player X')
        print('Player O')
        print('The game starts now.')
        while True:
            self.print_board()
            position = int(input('Player ' + self.current_player + ', choose your position (1-9): ')) - 1
            self.make_move(position)
            if self.check_win():
                self.print_board()
                print('Player ' + self.current_player + ' lost the game.')
                break
            elif self.check_draw():
                self.print_board()
                print('The game ended in a draw.')
                break

game = TicTacToe()
game.play_game()
