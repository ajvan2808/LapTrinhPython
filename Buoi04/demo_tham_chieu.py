def tham_chieu(ds: list):
    ds.extend([7, 8, 9])
    return ds


def tham_tri(x: int):
    x = 3
    return x


if __name__ == '__main__':
    ds = [4, 5, 6]
    print('danh sach truoc khi goi ham: ', ds)
    tham_chieu(ds)
    print('danh sach sau khi goi ham: ', ds)

    y = 5
    tham_tri(y)
    print(y)
