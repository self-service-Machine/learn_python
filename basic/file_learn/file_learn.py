
def write_file():
    file = open('../../data/message.txt', 'w')
    file.write('Hello World!\n')
    file.close()


def append_file():
    file = open('../../data/message.txt', 'a')
    file.write('Hello Everyone\n')
    file.close()


def read_file():
    with open('../../data/message.txt', 'r') as file:
        # 读取前9个字符(从开头读取文件)
        string1 = file.read(11)
        print(string1)

        # 移动文件指针到第x个字符
        file.seek(13)
        string2 = file.read(15)
        print(string2)


def read_file_line():
    print('\n', '=' * 39, 'read', '=' * 39, '\n')
    with open('../../data/message.txt', 'r') as file:
        number = 0
        while True:
            number += 1
            line = file.readline()
            if line == '':
                break
            print(number, line, end='\n')
    print('\n', '='*39, 'over', '='*39, '\n')


def read_all_lines():
    with open('../../data/message.txt', 'r') as file:
        # 读取全部行
        message = file.readlines()
        print(message)


if __name__ == '__main__':
    # 写文件
    # write_file()

    # 追加文件
    # append_file()

    # 读取文件
    # read_file()
    # 单行读取
    # read_file_line()
    # 读取全部行
    read_all_lines()
    pass
