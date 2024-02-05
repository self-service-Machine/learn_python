"""
@property 装饰器，将方法转换为属性

@property
def methodname(self):
    return self


类中的属性类型：

class Geese:
    wing = 'tttt'         类属性，可以在类的所有实例之间共享值，可以通过类名称或实例名访问
    def __init__ (self):
        self.name         实例属性，只作用于当前实例中
        self._foo         protected属性，只允许类本身和子类访问
        self.__age        private属性，只允许类本身访问，不能通过类的实例访问，可以通过类的实例名._类名__属性名访问

"""


class TVshow:
    list_films = ['Horror', 'Action', 'Love', 'Documentary']

    # 创建实例时自动执行的构造方法
    def __init__(self, show):
        # 创建了私有属性show
        self.__show = show
        self.name = 'test'

    # 将show()方法转换为属性调用
    @property
    def show(self):
        return self.__show

    # 利用setter对私有属性进行修改
    @show.setter
    def show(self, value):
        if value in TVshow.list_films:
            # 修改属性值
            self.__show = value
            print('you choose {}'.format(value))
        else:
            print('invalid, the film type: {} is not exist'.format(value))


if __name__ == '__main__':
    tv = TVshow('Horror')
    print(tv.show)
    tv.show = 'Action'
    print(tv.show)
    tv.show = 'Theology'
    print(tv.show)

    # 通过类访问私有属性
    print(tv._TVshow__show)
