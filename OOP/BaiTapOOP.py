class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._luong_cb = luong_cb
        self._luong_thang = 0

    def __str__(self):
        s = ("Ma nhan vien: {}\n"
             "Ten: {}\n"
             "Luong co ban: {}\n"
             "Luong thang: {}"
             "").format(self._ma_nv, self._ho_ten, self._luong_cb, self._luong_thang)
        print(s)

    @property
    def _luong_cb(self):
        return self.__luong_cb

    @_luong_cb.setter
    def _luong_cb(self, value):
        if value > 0:
            self.__luong_cb = value
        else:
            self.__luong_cb = 1450000


class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv: str, ho_ten: str, luong_cb: float, so_ngay) -> object:
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_ngay = so_ngay
        self.bo_phan = 'NVBH'

    def __str__(self):
        super().__str__()
        print(f'So ngay: {self.so_ngay}, Bo phan: {self.bo_phan}')

    def tinh_luong(self):
        self._luong_thang = self._luong_cb + (self.so_ngay*150.000)
        return self._luong_thang


class NhanVienBanHang(NhanVien):
    def __init__(self, ma_nv: str, ho_ten: str, luong_cb: float, so_sp) -> object:
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_sp = so_sp
        self.bo_phan = 'NVBH'

    def __str__(self):
        super().__str__()
        print(f'So san pham: {self.so_sp}, Bo phan: {self.bo_phan}')

    def tinh_luong(self):
        self._luong_thang = self._luong_cb + (self.so_sp * 18.000)
        return self._luong_thang


class CongTy:
    NVVP = 'NVVP'
    NVBH = 'NVBH'

    def __init__(self, ma_cong_ty, ten_cong_ty):
        self.__ma_cong_ty = ma_cong_ty
        self.__ten_cong_ty = ten_cong_ty
        self.__danh_sach_nv = {}
        self.__so_nv = 0

    def tao_du_lieu(self, ma_nv: str, ho_ten: str, luong_cb: float, amount: int, bo_phan: str):
        nhan_vien = object
        if bo_phan == CongTy.NVVP:
            nhan_vien = NhanVienVanPhong(ma_nv, ho_ten, luong_cb, amount)
        elif bo_phan == CongTy.NVBH:
            nhan_vien = NhanVienBanHang(ma_nv, ho_ten, luong_cb, amount)

        self.__danh_sach_nv.update({ma_nv: nhan_vien})
        self.__so_nv += 1

        return nhan_vien

    def show(self):
        print('------ Danh sach nhan vien ------')
        print(f'Tong so nhan vien: {self.__so_nv}')
        for nhan_vien in self.__danh_sach_nv.values():
            nhan_vien.__str__()
            print('--')
        print('---------------------------------')

    def tim_nhan_vien(self, ma_nv):
        if ma_nv in self.__danh_sach_nv:
            nhan_vien = self.__danh_sach_nv.get(ma_nv)
            return nhan_vien.__str__()
        else:
            return 'Khong co thong tin nhan vien can tim!'

    def tim_nhan_vien_luong_cao_nhat(self):
        nv_luong_max = max(self.__danh_sach_nv.values(), key=lambda nv: nv._luong_thang)
        print('Nhan vien luong cao nhat: ')
        nv_luong_max.__str__()

    def tim_nhan_vien_bh_luong_cao_nhat(self):
        nv_bh = filter(lambda nv: nv.bo_phan == CongTy.NVBH, self.__danh_sach_nv.values())
        nv_luong_max = max(nv_bh, key=lambda nv: nv._luong_thang)
        print('Nhan vien ban hang luong cao nhat la: ')
        nv_luong_max.__str__()

    def update_luong(self, ma_nv, luong_moi):
        nv = self.__danh_sach_nv.get(ma_nv)
        nv._luong_cb = luong_moi


if __name__ == '__main__':
    cty = CongTy(ma_cong_ty='CongTy2023', ten_cong_ty='TNHH')

    cty.show()

    nv1 = cty.tao_du_lieu('01', 'Sunny', 4000000,30, 'NVVP')
    nv2 = cty.tao_du_lieu('02', 'Teo', 0,30, 'NVBH')
    nv3 = cty.tao_du_lieu('03', 'Hanh', 5000000,28, 'NVBH')
    nv4 = cty.tao_du_lieu('04', 'Hong', 4000000,31, 'NVBH')
    nv5 = cty.tao_du_lieu('05', 'Tu', 3000000,31, 'NVVP')
    nv6 = cty.tao_du_lieu('06', 'Bong', 5000000,31, 'NVVP')

    print(nv2._luong_cb)

    cty.show()

    print(nv1.tinh_luong())
    print(nv2.tinh_luong())
    print(nv3.tinh_luong())
    print(nv4.tinh_luong())

    print(cty.tim_nhan_vien(ma_nv='01'))
    print(cty.tim_nhan_vien(ma_nv='07'))

    # sau khi tinh luong thang
    cty.show()
    cty.tim_nhan_vien_luong_cao_nhat()
    cty.tim_nhan_vien_bh_luong_cao_nhat()

    cty.update_luong('02', 3000000)
    nv2.__str__()
