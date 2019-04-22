import random, getch, os


class Game(object):
    def __init__(self):
        self.field = []
        num = 1
        for i in range(4):
            line = []
            for j in range(4):
                line.append(num)
                num += 1
            self.field.append(line)
        self.field[3][3] = 0

    def move_down(self):
        for i in range(4):
            for j in range(4):
                if self.field[i][j] == 0:
                    if i != 0:
                        self.field[i][j] = self.field[i-1][j]
                        self.field[i-1][j] = 0

    def move_left(self):
        for i in range(4):
            for j in range(4):
                if self.field[i][j] == 0:
                    if j != 3:
                        self.field[i][j] = self.field[i][j + 1]
                        self.field[i][j + 1] = 0
                        return

    def move_right(self):
        for i in range(4):
            for j in range(4):
                if self.field[i][j] == 0:
                    if j != 0:
                        self.field[i][j] = self.field[i][j - 1]
                        self.field[i][j - 1] = 0
                        return

    def move_up(self):
        for i in range(4):
            for j in range(4):
                if self.field[i][j] == 0:
                    if i != 3:
                        self.field[i][j] = self.field[i + 1][j]
                        self.field[i + 1][j] = 0
                        return

    def mix(self):
        for i in range(30):
            move = random.randint(0, 4)
            if move == 0:
                self.move_down()
            elif move == 1:
                self.move_left()
            elif move == 2:
                self.move_right()
            elif move == 3:
                self.move_up()

    def show(self):
        for i in range(4):
            for j in range(4):
                if game.field[i][j] < 10:
                    print(" ", end='')
                    print(game.field[i][j], end='')
                    print(' ', end='')
                else:
                    print(game.field[i][j], end='')
                    print(' ', end='')
            print("\n", end='')
        return

    def isWin(self):
        for i in range(4):
            for j in range(4):
                if i != 3 and j != 3:
                    if self.field[i][j] != j + i * 4 + 1:
                        return False
        if self.field[3][3] != 0:
            return False
        return True


if __name__ == '__main__':
    game = Game()
    game.mix()
    key = 0
    while key != 'z':
        print()
        os.system('clear')
        game.show()
        if game.isWin():
            print("Победа!!!")
            break
        key = getch.getch()
        if key == 'a':
            game.move_left()
        elif key == 's':
            game.move_down()
        elif key == 'd':
            game.move_right()
        elif key == 'w':
            game.move_up()

