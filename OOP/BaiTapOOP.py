class NhanVienVanPhong:
    def __init__(self, ma_nv: str, ho_ten: str, luong_cb: float) -> object:
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.luong_thang = 0
        self.bo_phan = 'NVBH'

    def __str__(self):
        return f"{self.ma_nv}, {self.ho_ten}, {self.luong_cb}, {self.luong_thang}"

    def tinh_luong_thang(self, amount):
        self.luong_thang = self.luong_cb + (amount*18.000)
        return self.luong_thang


class NhanVienBanHang:
    def __init__(self, ma_nv: str, ho_ten: str, luong_cb: float) -> object:
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.luong_thang = 0
        self.bo_phan = 'NVBH'

    def __str__(self):
        return f"{self.ma_nv}, {self.ho_ten}, {self.luong_cb}, {self.luong_thang}"

    def tinh_luong_thang(self, amount):
        self.luong_thang = self.luong_cb + (amount * 150.000)
        return self.luong_thang


class QuanLyNhanVien:
    NVVP = 'NVVP'
    NVBH = 'NVBH'

    def __init__(self):
        self.ds_nhan_vien = {}
        self.so_nhan_vien = 0

    def tao_nhan_vien(self, ma_nv: str, ho_ten: str, luong_cb: float, bo_phan: str):
        nhan_vien = object
        if bo_phan == QuanLyNhanVien.NVVP:
            nhan_vien = NhanVienVanPhong(ma_nv, ho_ten, luong_cb)
        elif bo_phan == QuanLyNhanVien.NVBH:
            nhan_vien = NhanVienBanHang(ma_nv, ho_ten, luong_cb)

        self.ds_nhan_vien.update({ma_nv: nhan_vien})
        self.so_nhan_vien += 1

        return nhan_vien

    def __str__(self):
        print('Danh sach nhan vien: ')
        for nhan_vien in self.ds_nhan_vien.values():
            print(f'{str(nhan_vien)}')
        print(f'Tong so nhan vien: {self.so_nhan_vien}')

    def tim_nhan_vien(self, ma_nv):
        if ma_nv in self.ds_nhan_vien:
            nhan_vien = self.ds_nhan_vien.get(ma_nv)
            return nhan_vien
        else:
            return 'Khong co thong tin nhan vien can tim!'

    def tinh_luong_thang(self, amount):
        for nhan_vien in self.ds_nhan_vien.values():
            nhan_vien.tinh_luong_thang(amount)

    def tim_nhan_vien_luong_cao_nhat(self):
        nv_luong_max = max(self.ds_nhan_vien.values(), key=lambda nv: nv.luong_thang)
        print(nv_luong_max)

    def tim_nhan_vien_bh_luong_cao_nhat(self):
        nv_bh = filter(lambda nv: nv.bo_phan == QuanLyNhanVien.NVBH, self.ds_nhan_vien.values())
        nv_luong_max = max(nv_bh, key=lambda nv: nv.luong_thang)
        print(f'Nhan vien ban hang luong cao nhat la: {nv_luong_max}')


if __name__ == '__main__':
    qlnv = QuanLyNhanVien()

    print(qlnv.__str__())

    nv1 = qlnv.tao_nhan_vien('01', 'Sunny', 4000000, 'NVVP')
    nv2 = qlnv.tao_nhan_vien('02', 'Teo', 3000000, 'NVBH')
    nv3 = qlnv.tao_nhan_vien('03', 'Hanh', 5000000, 'NVBH')
    nv4 = qlnv.tao_nhan_vien('04', 'Hong', 4000000, 'NVBH')

    print(qlnv.__str__())

    print(nv1.tinh_luong_thang(28))
    print(nv2.tinh_luong_thang(30))
    print(nv3.tinh_luong_thang(30))
    print(nv4.tinh_luong_thang(29))

    print(qlnv.tim_nhan_vien(ma_nv='01'))
    print(qlnv.tim_nhan_vien(ma_nv='05'))

    # sau khi tinh luong thang
    qlnv.__str__()
    qlnv.tim_nhan_vien_luong_cao_nhat()
    qlnv.tim_nhan_vien_bh_luong_cao_nhat()

    nvvp1 = qlnv.tao_nhan_vien('05', 'Nguyen Be Nam', 3000000, 'NVVP')
    nvvp2 = qlnv.tao_nhan_vien('06', 'Tran Thi Tu', 5000000, 'NVVP')

    print(nvvp1.tinh_luong_thang(30))
    print(nvvp2.tinh_luong_thang(29))

    print(qlnv.tim_nhan_vien('05'))
