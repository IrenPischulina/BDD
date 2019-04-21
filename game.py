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
