"""
某次战役中，为便于信息交互，我军侦察部门将此次战役的关键高地坐标设定为（x=0，y=0）并规定，每向东增加100米，x加1，每向北增加100米，y加1。
同时，我军情报部门也破译了敌军向坦克发送的指挥信号，其中有三种信号（L,R,M）用于控制坦克的运动，L 和 R 分别表示使令坦克向左、向右转向，M 表示令坦克直线开进100米，其它信号如T用于时间同步，P用于位置较准。
一日，我军侦察兵发现了敌军的一辆坦克，侦察兵立即将坦克所在坐标（P, Q）及坦克前进方向（W：西，E：东，N：北，S：南）发送给指挥部，同时启动信号接收器，将坦克接收到的信号实时同步发往指挥部，
指挥部根据这些信息得以实时掌控了该坦克的位置，并使用榴弹炮精准地击毁了该坦克。

请设计合理的数据结构和算法，根据坦克接收到的信号，推断出坦克所在的位置。
设计时请考虑可能的扩展情况，并体现出您的设计风格。

假设，侦察兵发送给指挥部的信息如下：
坦克坐标：（11，39）
坦克运行方向：W
坦克接收到的信号为：MTMPRPMTMLMRPRMTPLMMTLMRRMP
其位置应该是（9，43），运动方向为E
"""

class Tank:
    pointer = 'NESW'  # 方向指针
    shift = {'N': 'y+1', 'S': 'y-1', 'W': 'x-1', 'E': 'x+1'}  # 位移偏量

    def __init__(self, position, direction):
        self.x, self.y = position
        self.direction = direction
        self.position = (self.x, self.y)

    def signal(self, orders):
        for i in orders:
            if i in 'LR':
                self.turn(i)
            elif i == 'M':
                self.move()
            elif i == 'P':
                self.pd()

    def turn(self, orders):
        i = self.pointer.find(self.direction)
        if orders == 'L':
            i -= 1
        elif orders == 'R':
            i += 1
        self.direction = self.pointer[i % 4]

    def move(self):
        orders = self.shift[self.direction]
        if orders[0] == 'x':
            x = self.x
            self.x = eval(orders)
        else:
            y = self.y
            self.y = eval(orders)
        self.position = (self.x, self.y)

    def pd(self):
        print(self.position, self.direction)


tank = Tank((11, 39), 'W')
tank.signal('MTMPRPMTMLMRPRMTPLMMTLMRRMP')
