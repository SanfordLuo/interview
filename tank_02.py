class Tank:
    pointer_str = 'NESW'   # 方向
    x_shift = {'E': 1, 'W': -1}
    y_shift = {'N': 1, 'S': -1}

    def __init__(self, x, y, d):
        """
        :param x: x轴
        :param y: y轴
        :param d: 方向
        """
        self.x = x
        self.y = y
        self.d = d

    def turn(self, i):
        index = self.pointer_str.index(self.d)
        if i == 'L':
            index -= 1
        else:
            index += 1
        self.d = self.pointer_str[index % 4]

    def move(self):
        if self.d in self.x_shift.keys():
            self.x += self.x_shift[self.d]
        else:
            self.y += self.y_shift[self.d]

    def main(self, signal):
        for i in signal:
            if i in 'LR':
                self.turn(i)
            elif i == 'M':
                self.move()
            elif i == 'P':
                print(self.x, self.y, self.d)


if __name__ == '__main__':
    tank = Tank(11, 39, 'W')
    tank.main('MTMPRPMTMLMRPRMTPLMMTLMRRMP')
