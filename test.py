class Cat(object):
    def __init__(self, x, y, z):
        self.颜色 = x
        self.奔跑_速度 = y
        self.hhh = z

    def chi(self):
        self.sen = f'{self.颜色}的猫以{self.奔跑_速度}的速度再跑'

    def pao(self):
        print(self.sen)

    @staticmethod
    def xxx(x, y):
        print(x, y)


# bai_mao = Cat('白色', '7m/s')
# print(bai_mao.颜色)
# print(bai_mao.奔跑_速度)
# bai_mao.chi()
# print(bai_mao.sen)
Cat.xxx(1, 2)
sen = chi()
pao(sen)
