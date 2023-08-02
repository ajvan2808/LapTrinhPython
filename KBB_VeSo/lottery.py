import random
import string

co_cau_quay_so = {
    'DB': 1,
    'Nhat': 1,
    'Nhi': 1,
    'Ba': 2,
    'Tu': 7,
    'Nam': 1,
    'Sau': 3,
    'Bay': 1,
    'Tam': 1
}

so_do = {
    'DB': 6,
    'Nhat': 5,
    'Nhi': 5,
    'Ba': 5,
    'Tu': 5,
    'Nam': 4,
    'Sau': 4,
    'Bay': 3,
    'Tam': 2
}

def lottery():
    # buyer_num = input('Nhap so da mua: ')
    # while not buyer_num.isdigit() or len(buyer_num) != 6:
    #     print('Dinh dang khong dung, vui long nhap lai:')
    #     buyer_num = input('Nhap so da mua: ')

    try:

        for giai, lan_quay in co_cau_quay_so.items():
            kq = quay_so(lan_quay,giai)
            so_duoi = so_do.get(giai)
            print(kq)
            buyer_num = input('Nhap so da mua: ')

            if giai == 'DB' and buyer_num == kq[0]:
                print(f'Chuc mung ban da trung Giai {giai}.')
            elif giai in ['Nhat', 'Nhi', 'Ba', 'Tu']:
                for s in kq:
                    if buyer_num[-so_duoi:] == s:
                        print(f'Chuc mung ban da trung Giai {giai}.')
            elif giai in ['Nam', 'Sau']:
                for s in kq:
                    if buyer_num[-so_duoi:] == s:
                        print(f'Chuc mung ban da trung Giai {giai}.')
            elif giai == 'Bay':
                if buyer_num[-so_duoi:] == kq[0]:
                    print(f'Chuc mung ban da trung Giai {giai}.')
            elif giai == 'Tam':
                if buyer_num[-so_duoi:] == kq[0]:
                    print(f'Chuc mung ban da trung Giai {giai}.')
            else:
                print('Rat tiec, ban khong trung giai.')

    except KeyboardInterrupt:
        raise KeyboardInterrupt('Errors occurred!')


def quay_so(n, giai):
    lst = []
    so_duoi = so_do.get(giai)
    for i in range(n):
        lst.append(''.join(random.choices(string.digits, k=so_duoi)))
    return lst


if __name__ == '__main__':
    lottery()
