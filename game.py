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
