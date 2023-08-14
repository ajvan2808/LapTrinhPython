def addition(x, y):
    return x + y


def add_default_args(x=3, y=4):
    return x + y


def add_keyword_args(x=0, y=1):
    return x + y


if __name__ == '__main__':
    print(addition(4, 5))
    # Báo lỗi do thiếu đối số
    # print(addition(4))

    print(add_default_args())
    print(add_default_args(5))
    print(add_default_args(6, 7))

    print(add_keyword_args(x=0.5, y=5))
    print(add_keyword_args(y=4, x=4))
