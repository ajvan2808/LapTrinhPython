ID = 'ID'
HO_TEN = 'HO_TEN'
LUONG_CB = 'LUONG_CO_BAN'
LUONG_TH = 'LUONG_THANG'
LOAI_NV = 'LOAI_NHAN_VIEN'
fields = [ID, HO_TEN, LUONG_CB, LUONG_TH, LOAI_NV]
employee_list = []


def create_employee(id, hoTen, luongCB, empType):
    employee_info = dict.fromkeys(fields, None)
    employee_info[ID] = id
    employee_info[HO_TEN] = hoTen
    employee_info[LUONG_CB] = luongCB
    employee_info[LUONG_TH] = 0
    employee_info[LOAI_NV] = empType

    employee_list.append(employee_info)

    return employee_info


def search_employee(id) -> dict:
    for i in employee_list:
        if i.get(ID) == id:
            return i


def calculate_month_salary(id, amount):
    employee = search_employee(id)
    salary = employee.get(LUONG_CB)
    if employee.get(LOAI_NV) == 'NV_VP':
        amount *= 150.000
    elif employee.get(LOAI_NV) == 'NV_BH':
        amount *= 18000

    monthly_salary = salary + amount
    # update luong thang
    employee[LUONG_TH] = monthly_salary
    return monthly_salary


def display_info(id: str):
    employee = search_employee(id)
    ho_ten = employee.get(HO_TEN)
    luong_cb = employee.get(LUONG_CB)
    luong_thang = employee.get(LUONG_TH)
    if not employee:
        print("Employee doesn't exist")
    else:
        print(f'ID: {ID}\n'
              f'Name: {ho_ten}\n'
              f'Luong co ban: {format(luong_cb, ",.0f")}\n'
              f'Luong thang: {format(luong_thang, ",.0f")}')


def find_the_highest_paid():
    highest_paid_employee = max(employee_list, key=lambda employee: employee[LUONG_TH])
    return highest_paid_employee


def find_lowest_sale_person():
    nv_bh_list = list(filter(lambda employee: employee[LOAI_NV] == 'NV_BH', employee_list))
    the_lowest = min(nv_bh_list, key=lambda employee: employee[LUONG_TH])
    return the_lowest


if __name__ == '__main__':
    create_employee('01', 'Sunny', 5000000, 'NV_VP')
    create_employee('02', 'Sang', 4000000, 'NV_BH')
    create_employee('03', 'Hana', 5000000, 'NV_VP')
    create_employee('04', 'Steve', 4000000, 'NV_BH')
    create_employee('05', 'Meow', 5000000, 'NV_VP')

    display_info('03')

    calculate_month_salary('01', 30)
    calculate_month_salary('02', 28)
    calculate_month_salary('03', 30)
    calculate_month_salary('05', 30)
    calculate_month_salary('04', 15)

    display_info('05')
    display_info('03')

    print(find_the_highest_paid())
    print(find_lowest_sale_person())
