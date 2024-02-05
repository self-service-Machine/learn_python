
class Fruit:
    # color = 'green'

    def __init__(self, color='green'):
        Fruit.color = color

    def harvest(self, color):
        print("fruit's color is " + color)
        print("fruit's source color is " + Fruit.color)


class Apple(Fruit):
    color = 'red'

    def __init__(self):
        super().__init__()
        print('I am an Apple')


class Orange(Fruit):
    color = 'orange'

    def __init__(self):
        # 派生类调用基类的__init__()进行必要的初始化
        super().__init__()
        print('I am an Orange')

    # 方法重写
    def harvest(self, color):
        print("orange's color is " + color)
        print("orange's source color is " + Fruit.color)


class Sapodilla(Fruit):

    def __init__(self, color):
        print('I am a Sapodilla')
        super().__init__(color)

    def harvest(self, color):
        print("Sapodilla's color is " + color)
        print("Sapodilla's source color is" + Fruit.color)


if __name__ == '__main__':
    apple = Apple()
    apple.harvest(apple.color)

    orange = Orange()
    orange.harvest(orange.color)

    sapodilla = Sapodilla('white')
    sapodilla.harvest('yello')
