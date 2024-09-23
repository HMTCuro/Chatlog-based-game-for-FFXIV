#播棋
class Sowing():
    def __init__(self):
        # self.chessBoard=[0,4,4,4,4,4,4,0,4,4,4,4,4,4]
        self.chessBoard = [0, 1, 2, 3, 4, 5, 4, 0, 1, 2, 3, 4, 4, 4]

    def draw(self):
        numstr = ''
        print('                          ')
        print('┏━┓┏━┓┏━┓┏━┓┏━┓┏━┓┏━┓┏━┓')
        s = '  '
        for i in range(7):
            if i == 0:
                n = self.chessBoard[0]
                s += numstr[n // 10] + numstr[n % 10] + '    '
            else:
                n = self.chessBoard[14 - i]
                s += numstr[n // 10] + numstr[n % 10] + '    '
        print(s)
        print('            ┗━┛┗━┛┗━┛┗━┛┗━┛┗━┛')

        print('            ┏━┓┏━┓┏━┓┏━┓┏━┓┏━┓')
        s = '              '
        for i in range(7):
            n = self.chessBoard[i + 1]
            s += numstr[n // 10] + numstr[n % 10] + '    '
        print(s)
        print('┗━┛┗━┛┗━┛┗━┛┗━┛┗━┛┗━┛┗━┛')
        print('                                      ')

    def move(self, pos):
        if pos != 0 and pos != 7:
            index = pos + 1
            n = self.chessBoard[pos]
            self.chessBoard[pos] = 0
            for i in range(n):
                if index == 14:
                    index -= 14
                self.chessBoard[index] += 1
                index += 1
            index -= 1
            if self.chessBoard[index] == 1:
                if 0 < pos < 7 and 0 < index < 7:
                    self.chessBoard[7] += (1 + self.chessBoard[14 - index])
                    self.chessBoard[index] = 0
                    self.chessBoard[14 - index] = 0
                elif 7 < pos < 14 and 7 < index < 14:
                    self.chessBoard[0] += (1 + self.chessBoard[14 - index])
                    self.chessBoard[index] = 0
                    self.chessBoard[14 - index] = 0

    def readOrder(self, s):
        strings = ['A0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'BO', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1']
        if s in strings:
            return strings.index(s)
        return 0

    def start(self):
        self.draw()
        end=False
        cntA=0
        cntB=0
        while not end:
            s=input('输入移动项')
            if s=='END':
                cntA=self.chessBoard[0]+sum(self.chessBoard[8:])
                cntB=sum(self.chessBoard[1:8])
                end=True
            else:
                self.move(self.readOrder(s))
            self.draw()
        print(cntA,cntB)

c = Sowing()
c.start()
