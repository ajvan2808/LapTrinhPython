class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._luong_cb = luong_cb
        self._luong_thang = 0

    def show(self):
        print(f'Thong tin nhan vien: {self._ma_nv}, {self._ho_ten}, {self._luong_cb}')


class NhanVienKinhDoanh(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.__so_sp = so_sp

    def show(self):
        super().show()
        print(self.__so_sp)

    def tinh_luong(self):
        self._luong_thang = self._luong_cb + (self.__so_sp * 18.000)
        return self._luong_thang


class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_ngay):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.__so_ngay = so_ngay
    
    def show(self):
        super().show()
        print(self.__so_ngay)


class CongTy:
    NVVP = 'NVVP'
    NVBH = 'NVBH'

    def __init__(self, ma_cong_ty, ten_cong_ty):
        self.__ma_cong_ty = ma_cong_ty
        self.__ten_cong_ty = ten_cong_ty
        self.__danh_sach_nv = {}

    def tao_du_lieu(self, ma_nv: str, ho_ten: str, luong_cb: float, bo_phan: str):
        nhan_vien = object
        if bo_phan == CongTy.NVVP:
            nhan_vien = NhanVienVanPhong(ma_nv, ho_ten, luong_cb, 0)
        elif bo_phan == CongTy.NVBH:
            nhan_vien = NhanVienKinhDoanh(ma_nv, ho_ten, luong_cb, 0)

        self.__danh_sach_nv.update({ma_nv: nhan_vien})
        # self.so_nhan_vien += 1

        return nhan_vien


vp1 = NhanVienVanPhong('001', 'Nguyen Thi Be', 2000, 20)
kd1 = NhanVienKinhDoanh('002', 'Nguyen Van B', 3000, 200)

vp1.show()
kd1.show()


# them tinh nang cap nhat luong co ban theo ma nhan vien