import random


def kbb():
    action = int(input("1: Bắt đầu, 0: Kết thúc "))
    while action == 1:
        try:
            m_sign = machine()
            urs = input('Bạn chọn kéo, búa hay bao?: ')
            if urs == '0':
                break

            if (urs == 'keo' and m_sign == 'keo') or \
                    (urs == 'bua' and m_sign == 'bua') or \
                    (urs == 'bao' and m_sign == 'bao'):
                print(f'machine: {m_sign} - Hòa')

            elif (urs == 'bua' and m_sign == 'keo') or \
                    (urs == 'bao' and m_sign == 'bua') or \
                    (urs == 'keo' and m_sign == 'bao'):
                print(f'machine: {m_sign} - Ban thang')

            # elif (urs == 'keo' and m_sign == 'bua') or \
            #         (urs == 'bua' and m_sign == 'bao') or \
            #         (urs == 'bao' and m_sign == 'keo'):
            else:
                print(f'machine: {m_sign} - Ban thua')
        except KeyboardInterrupt:
            print('Some errors occur!')


def machine():
    ls = ['keo', 'bua', 'bao']
    return random.choice(ls)


if __name__ == '__main__':
    kbb()
