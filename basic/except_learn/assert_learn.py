"""
python -O 执行python程序时会跳过assert处理

"""

def division():
    print()
    apple = int(input('Enter a number of apple: '))
    children = int(input('Enter a number of children: '))
    assert apple > children, 'The apple must be more than the children'
    # 调用整除
    result = apple // children
    remain = apple - result * children
    if remain > 0:
        print(apple, 'apple to ', children, 'children, everyone has ', result, 'remain ', remain)
    else:
        print(apple, 'apple to ', children, 'children, everyone has ', result)


if __name__ == '__main__':
    try:
        division()
    except AssertionError as e:
        print('You entered number is error: ', e)
