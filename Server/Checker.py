from Move_checker import move_checkers


class Checker:
    def __init__(self):
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [2, 0, 2, 0, 2, 0, 2, 0],
                      [0, 2, 0, 2, 0, 2, 0, 2],
                      [2, 0, 2, 0, 2, 0, 2, 0]]
        self.black = (1, 3)
        self.white = (2, 4)
        self.empty = 0
        self.active_player = self.white
        self.inactive_player = self.black

    def move(self, x1, y1, x2, y2, player):
        #x1, y1 = x1 - 1, y1 - 1
        #x2, y2 = x2 - 1, y2 - 1
        if x1 == x2 or y1 == y2:
            return False
        if self.board[y1][x1] == self.empty:
            return False
        if (self.board[y1][x1] not in self.active_player) or (player not in self.active_player):
            return False
        if self.board[y1][x1] == self.active_player[0]:
            if (x2 - x1 == 1 or x2 - x1 == -1) and (y2 - y1 == 1 or y2 - y1 == -1):
                if self.board[y2][x2] == self.empty:
                    self._step(x1, y1, x2, y2)
                    return True
            elif (x2 - x1 == 2 or x2 - x1 == -2) and (y2 - y1 == 2 or y2 - y1 == -2):
                if self.board[y2][x2] == self.empty:
                    if self.board[y1 + (y2 - y1) // 2][x1 + (x2 - x1) // 2]:
                        self._step(x1, y1, x2, y2)
                        self._destroy(abs(x2 - x1) // 2, abs(y2 - y1) // 2)
                        print(2)
                        return True
        elif self.board[y1][x1] == self.active_player[1]:
            if x2 - x1 == y2 - y1 or x2 - x1 == y1 - y2:
                if self.board[y2][x2] == self.empty:
                    possible_step = False
                    possible_eat = False
                    sign_x = int(x2 - x1 > 0) * 2 - 1
                    sign_y = int(y2 - y1 > 0) * 2 - 1
                    for i in range(1, (x2 - x1) * sign_x):
                        if self.board[y1 + sign_y * i][x1 + sign_x * i] in self.active_player:
                            possible_step = False
                            possible_eat = False
                            break
                        elif self.board[y1 + sign_y * i][x1 + sign_x * i] not in self.active_player and \
                                self.board[y1 + sign_y * i][x1 + sign_x * i] != self.empty:
                            possible_eat = True
                            possible_step = True
                    if possible_step:
                        if possible_eat:
                            self._step(x1, y1, x2, y2)
                            for i in range(1, (x2 - x1) * sign_x):
                                self._destroy(x1 + sign_x * i, y1 + sign_y * i)
                                print(3)
                            return True
                        else:
                            self._step(x1, y1, x2, y2)
                            print(4)
                            return True
        print(10)
        return False

    def _step(self, x1, y1, x2, y2):
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = self.empty
        move_checkers(x1+1, y1+1, x2+1, y2+1)

    def _destroy(self, x, y):
        self.board[y][x] = self.empty
        move_checkers(x+1, y+1, 0, 0)

    def change_player(self):
        if self.active_player == self.white:
            self.active_player = self.black
            self.inactive_player = self.white
        elif self.active_player == self.black:
            self.active_player = self.white
            self.inactive_player = self.black
        else:
            raise Exception("active player not exist")

    def _check_for_eat(self, x, y):
        if self.board[y][x] == self.active_player[0]:
            if x + 2 < 8 and y + 2 < 8:
                if self.board[y + 1][x + 1] in self.inactive_player and \
                        self.board[y + 2][x + 2] in self.empty:
                    return True
            elif x - 2 >= 0 and y + 2 < 8:
                if self.board[y + 1][x - 1] in self.inactive_player and \
                        self.board[y + 2][x - 2] in self.empty:
                    return True
            elif x - 2 >= 0 and y - 2 >= 0:
                if self.board[y - 1][x - 1] in self.inactive_player and \
                        self.board[y - 2][x - 2] in self.empty:
                    return True
            elif x + 2 < 8 and y - 2 >= 0:
                if self.board[y - 1][x + 1] in self.inactive_player and \
                        self.board[y - 2][x + 2] in self.empty:
                    return True
            else:
                return False
        elif self.board[y][x] == self.active_player[1]:
            for i in range(1, 8):
                if x + i + 1 < 8 and y + i + 1 < 8:
                    if self.board[y + i][x + i] in self.inactive_player and \
                            self.board[y + i + 1][x + i + 1] in self.empty:
                        return True
                    elif self.board[y + i][x + i] in self.active_player:
                        break
            for i in range(1, 8):
                if x - i - 1 >= 0 and y + i + 1 < 8:
                    if self.board[y + i][x - i] in self.inactive_player and \
                            self.board[y + i + 1][x - i - 1] in self.empty:
                        return True
                    elif self.board[y + i][x - i] in self.active_player:
                        break
            for i in range(1, 8):
                if x - i - 1 >= 0 and y - i - 1 >= 0:
                    if self.board[y - i][x - i] in self.inactive_player and \
                            self.board[y - i - 1][x - i - 1] in self.empty:
                        return True
                    elif self.board[y - i][x - i] in self.active_player:
                        break
            for i in range(1, 8):
                if x + i + 1 < 8 and y - i - 1 >= 0:
                    if self.board[y - i][x + i] in self.inactive_player and \
                            self.board[y - i - 1][x + i + 1] in self.empty:
                        return True
                    elif self.board[y - i][x + i] in self.active_player:
                        break
            return False

    def set_white(self, player):
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                if self.board[y][x] == self.white[0]:
                    self.board[y][x] = player[0]
                elif self.board[y][x] == self.white[1]:
                    self.board[y][x] = player[1]
        if self.active_player == self.white:
            self.active_player = player
        self.white = player

    def set_black(self, player):
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                if self.board[y][x] == self.black[0]:
                    self.board[y][x] = player[0]
                elif self.board[y][x] == self.black[1]:
                    self.board[y][x] = player[1]
        if self.active_player == self.black:
            self.active_player = player
        self.black = player
