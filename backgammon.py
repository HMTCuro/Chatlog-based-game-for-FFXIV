# 双陆棋

class Backgammon():
    def __init__(self):
        """black+0 white-1"""
        self.destination = [0, 0]
        self.gather = [False, False]
        self.chessBoard = [0, -2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, -5, 0, 0, 0, 0, 2, 0]
        # self.chessBoard = [0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -15, 0, 0, 0, 0, 0, 0]
        # print(len(self.chessBoard))

    def draw(self):
        numstr = "─⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂"
        print(f"终点：●x{numstr[self.destination[0]]}┃○x{numstr[self.destination[1]]}")
        print("    ┃┃○起点/●终点")
        s1 = ''
        s2 = ''
        for i in range(13):
            if self.chessBoard[i] > 0:
                s1 = '●' + s1
                s2 = numstr[self.chessBoard[i]] + s2
            elif self.chessBoard[i] < 0:
                s1 = '○' + s1
                s2 = numstr[-self.chessBoard[i]] + s2
            else:
                s1 = '│' + s1
                s2 = numstr[0] + s2
        s1 = s1[:6] + '┃' + s1[6:12] + '┃' + s1[12]
        s2 = s2[:6] + '┃' + s2[6:12] + '┃' + s2[12]
        print('' + s1)
        print('┌' + s2)
        print("│                        ┃                        ┃")
        s1 = ''
        s2 = ''
        for i in range(13):
            if self.chessBoard[i + 13] > 0:
                s1 = s1 + '●'
                s2 = s2 + numstr[self.chessBoard[i + 13]]
            elif self.chessBoard[i + 13] < 0:
                s1 = s1 + '○'
                s2 = s2 + numstr[-self.chessBoard[i + 13]]
            else:
                s1 = s1 + '│'
                s2 = s2 + numstr[0]
        s1 = s1[:6] + '┃' + s1[6:12] + '┃' + s1[12]
        s2 = s2[:6] + '┃' + s2[6:12] + '┃' + s2[12]
        print('└' + s2)
        print('' + s1)
        print("    ┃┃●起点/○终点")

    def move(self, numOrder):
        step, index = numOrder
        if self.chessBoard[index] > 0:
            if index - step > 0:
                if self.chessBoard[index - step] >= 0:
                    self.chessBoard[index] -= 1
                    self.chessBoard[index - step] += 1
                elif self.chessBoard[index - step] == -1:
                    self.chessBoard[index] -= 1
                    self.chessBoard[index - step] = 1
                    self.chessBoard[0] -= 1
            else:
                if self.gather[0]:
                    self.chessBoard[index] -= 1
                    self.destination[0] += 1
        elif self.chessBoard[index] < 0:
            if index + step < 25:
                if self.chessBoard[index + step] <= 0:
                    self.chessBoard[index] += 1
                    self.chessBoard[index + step] -= 1
                elif self.chessBoard[index + step] == 1:
                    self.chessBoard[index] += 1
                    self.chessBoard[index + step] = -1
                    self.chessBoard[25] += 1
            else:
                if self.gather[1]:
                    self.chessBoard[index] += 1
                    self.destination[1] += 1
        return

    def readOrder(self, order):
        step = int(order[0])
        if order[1] == 'A':
            pos = int(order[2:])
            if pos == 0:
                index = 0
            else:
                index = 13 - pos
        else:
            pos = int(order[2:])
            if pos == 0:
                index = 25
            else:
                index = 12 + pos
        return step, index

    def check(self):
        baseB = 0
        baseW = 0
        for i in range(6):
            if self.chessBoard[i + 1] > 0:
                baseB += self.chessBoard[i + 1]
            if self.chessBoard[24 - i] < 0:
                baseW += self.chessBoard[24 - i]
        if baseB == 15-self.destination[0]:
            self.gather[0] = True
        else:
            self.gather[0] = False
        if baseW == -15+self.destination[1]:
            self.gather[1] = True
        else:
            self.gather[1] = False

    def start(self):
        self.draw()
        end = False
        win = ''
        while not end:
            s = input('输入指令步数+区块名（2A1）：')
            self.move(self.readOrder(s))
            self.draw()
            self.check()
            if self.destination[0] == 15:
                win = '●'
                end = True
            elif self.destination[1] == 15:
                win = '○'
                end = True
        print(win+"方获胜")


c = Backgammon()
c.start()
