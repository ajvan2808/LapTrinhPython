def calculate(a: float, b: float) -> tuple:
    """
    Calculate a and b
    :param a: float
    :param b: float
    :return: tuple, all results
    """
    cong = a + b
    tru = a - b
    nhan = a * b
    chia = a/b

    return cong, tru, nhan, chia


if __name__ == '__main__':
    # print(calculate(3, 4))
    cong, tru, nhan, chia = calculate(3, 4)
    print(f'cong = {cong}, tru = {tru}, nhan = {nhan}, chia = {chia}')
    print(calculate.__doc__)
