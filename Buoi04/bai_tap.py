# 01
import math


def tinh_tong_nhieu_so(*nums):
    tong = 0
    tich = 1
    for num in nums:
        tong += num
        tich *= num

    return tong, tich


def tinh_chuvi(**kwargs):
    chu_vi = 0
    dien_tich = 0
    if kwargs.get('hinh_vuong'):
        canh = kwargs.get('canh')
        chu_vi = canh * 4
        dien_tich = canh * canh

    elif kwargs.get('hinh_chu_nhat'):
        dai = kwargs.get('dai')
        rong = kwargs.get('rong')
        chu_vi = (dai + rong) * 2
        dien_tich = dai * rong

    elif kwargs.get('hinh_tron'):
        r = kwargs.get('r')
        chu_vi = 2 * math.pi * r
        dien_tich = 2 * math.pi * pow(r, 2)

    return chu_vi, dien_tich


def tinh_chuvi_dientich(*args, **kwargs):
    chu_vi = 0
    dien_tich = 0
    if kwargs.get('tinh') == 'chu vi':
        if kwargs.get('hinh_vuong'):
            canh = args[0]
            chu_vi = canh * 4

        elif kwargs.get('hinh_chu_nhat'):
            dai = args[0]
            rong = args[1]
            chu_vi = (dai + rong) * 2

        elif kwargs.get('hinh_tron'):
            r = args[0]
            chu_vi = round(2 * math.pi * r, 2)

        return chu_vi

    elif kwargs.get('tinh') == 'dien tich':
        if kwargs.get('hinh_vuong'):
            canh = args[0]
            dien_tich = canh * canh

        elif kwargs.get('hinh_chu_nhat'):
            dai = args[0]
            rong = args[1]
            dien_tich = dai * rong

        elif kwargs.get('hinh_tron'):
            r = args[0]
            dien_tich = round(2 * math.pi * pow(r, 2), 2)

        return dien_tich


print(tinh_tong_nhieu_so(2, 3, 6, 9))
print(tinh_chuvi(hinh_chu_nhat=True, dai=5, rong=3))
print(tinh_chuvi_dientich(3, tinh='dien tich', hinh_tron=True))
