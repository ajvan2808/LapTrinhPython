class NHANVIEN:
    # thuoc tinh cua class duoc goi ben trong class tu chinh ten class do hoac bang ten object
    so_nhan_vien = 100

    def __init__(self, maNV: int, ho_ten: str, luong_cb: int):
        self.maNV = maNV
        self.hoTen = ho_ten
        self.luongCB = luong_cb

    def __repr__(self):
        return '''
        Ma nhan vien: {} 
        Ho ten: {} 
        Luong co ban: {} 
        '''.format(self.maNV, self.hoTen, self.luongCB)

    @classmethod
    def so_luong_nv(cls):
        return f'Class method tra ve so luong nv: {cls.so_nhan_vien}'

    @staticmethod
    def thue_ca_nhan(amount: float):
        return amount * 0.1


if __name__ == '__main__':
    nv1 = NHANVIEN(1, 'Van Hoa Sunny', 1000000)
    print(nv1.__repr__())
    print('Thuoc tinh so_nhan_vien cua class goi tu class: ', NHANVIEN.so_nhan_vien)
    print('Thuoc tinh so_nhan_vien cua class goi tu instance object: ', nv1.so_nhan_vien)

    # Cach goi class method
    print(nv1.so_luong_nv(), '- goi tu object')
    print(NHANVIEN.so_luong_nv(), '- goi tu class')

    # cach goi static method
    print('Co the goi static method tu class: ', NHANVIEN.thue_ca_nhan(3000))
    print('Co the goi static method tu object: ', nv1.thue_ca_nhan(3000))

