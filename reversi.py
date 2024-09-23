# 黑白棋
import numpy as np

class Reversi():
    def __init__(self):
        l = [-1 for _ in range(64)]
        chessboard = np.array(l)
        self.chessboard = chessboard.reshape(8, 8)
        self.chessboard[3, 3], self.chessboard[3, 4], self.chessboard[4, 3], self.chessboard[4, 4] = 0, 1, 1, 0

    def draw(self):
        squareLetters = ''
        print("    ")
        for i in range(8):
            str = '' + squareLetters[i]
            for j in range(8):
                if self.chessboard[i, j] == 0:
                    str += '●'
                elif self.chessboard[i, j] == 1:
                    str += '○'
                else:
                    str += '─'
            print(str)

        return 0

    def colCheck(self, side, coord):
        # up check
        x, y = coord
        index = x - 1
        stack = []
        while index >= 0:
            if self.chessboard[index, y] == -1:
                break
            elif self.chessboard[index, y] != side:
                stack.append(index)
                index -= 1
            else:
                for i in stack:
                    self.chessboard[i, y] = side
                break
        # down check
        index = x + 1
        stack = []
        while index < 8:
            if self.chessboard[index, y] == -1:
                break
            elif self.chessboard[index, y] != side:
                stack.append(index)
                index += 1
            else:
                for i in stack:
                    self.chessboard[i, y] = side
                break

    def rowCheck(self, side, coord):
        # left check
        x, y = coord
        index = y - 1
        stack = []
        while index >= 0:
            if self.chessboard[x, index] == -1:
                break
            elif self.chessboard[x, index] != side:
                stack.append(index)
                index -= 1
            else:
                for i in stack:
                    self.chessboard[x, i] = side
                break
        # right check
        index = y + 1
        stack = []
        while index < 8:
            if self.chessboard[x, index] == -1:
                break
            elif self.chessboard[x, index] != side:
                stack.append(index)
                index += 1
            else:
                for i in stack:
                    self.chessboard[x, i] = side
                break

    def xCheck(self, side, coord):
        # left up check
        x, y = coord
        indexX = x - 1
        indexY = y - 1
        stack = []
        while indexX >= 0 and indexY >= 0:
            if self.chessboard[indexX, indexY] == -1:
                break
            elif self.chessboard[indexX, indexY] != side:
                stack.append((indexX, indexY))
                indexX -= 1
                indexY -= 1
            else:
                for i in stack:
                    xi, yi = i
                    self.chessboard[xi, yi] = side
                break
        # left down check
        indexX = x + 1
        indexY = y - 1
        stack = []
        while indexX < 8 and indexY >= 0:
            if self.chessboard[indexX, indexY] == -1:
                break
            elif self.chessboard[indexX, indexY] != side:
                stack.append((indexX, indexY))
                indexX += 1
                indexY -= 1
            else:
                for i in stack:
                    xi, yi = i
                    self.chessboard[xi, yi] = side
                break
        # right up check
        indexX = x - 1
        indexY = y + 1
        stack = []
        while indexX >= 0 and indexY < 8:
            if self.chessboard[indexX, indexY] == -1:
                break
            elif self.chessboard[indexX, indexY] != side:
                stack.append((indexX, indexY))
                indexX -= 1
                indexY += 1
            else:
                for i in stack:
                    xi, yi = i
                    self.chessboard[xi, yi] = side
                break
        # right down check
        indexX = x + 1
        indexY = y + 1
        stack = []
        while indexX < 8 and indexY < 8:
            if self.chessboard[indexX, indexY] == -1:
                break
            elif self.chessboard[indexX, indexY] != side:
                stack.append((indexX, indexY))
                indexX += 1
                indexY += 1
            else:
                for i in stack:
                    xi, yi = i
                    self.chessboard[xi, yi] = side
                break

    def place(self, side, coord):
        x, y = coord
        self.chessboard[x, y] = side
        self.colCheck(side, coord)
        self.rowCheck(side, coord)
        self.xCheck(side, coord)
        self.draw()

    def s2coordinate(self, string):
        letters = list("ABCDEFGH")
        return letters.index(string[0]), int(string[1]) - 1

    def start(self):
        end = False
        self.draw()
        while not end:
            s = input("输入指令：●黑:0|○白:1+坐标（如0A1）或“END”")
            if s == 'END':
                end = True
                continue
            side = int(s[0])
            coord = self.s2coordinate(s[1:])
            self.place(side, coord)
        bn = 0
        wn = 0
        for i in range(8):
            for j in range(8):
                if self.chessboard[i, j] == 0:
                    bn += 1
                elif self.chessboard[i, j] == 1:
                    wn += 1
        print(f"结果为：黑棋{bn}枚-白棋{wn}枚")


c = Reversi()
c.start()
