from VMI import Vendor1
from Parameters import Parameters
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


# ghi du lieu vao file txt
def showinfile(T, i, j, k, q1, q2, q3, THC1, THC2, TOC, TPC2, TRC, TSC1, TSC2, TCp):
    f = open("dataout/loop %s.txt" % T, "a")  # tạo file txt ứng với mỗi vòng lặp
    str1 = ''  # khai báo chuỗi rỗng
    arr = np.array([T, i, j, k, q1, q2, q3, THC1, THC2, TOC, TPC2, TRC, TSC1, TSC2, TCp])  # khai báo mảng
    for i in arr:
        str1 += str(i) + ": "  # chuyển từ số sang chuỗi r cộng vào chuỗi
    f.write(str1 + "\n")


y = np.array([], dtype='i')  # trục y của đồ thị là giá trị tcp
x = np.array([], dtype='i')  # trục x của đồ thị là T


def loop(T):
    global y  # do biến y là biến toàn cục bên trong hàm có thay đổi giá trị của y nên phải sử dụng global
    arr1 = np.array([], dtype='i')  # mảng chưa dữ liệu mỗi khi vòng lặp thay đổi
    arr2 = np.array([], dtype='i')  # mảng chứa tcp của mỗi lần lặp
    str1 = ''  # chuỗi trả về
    mintcp = 99999999
    for i in range(1, T + 1):
        for j in range(1, T + 1):
            for k in range(1, T + 1):
                 #công thức tính
                q1 = round(vd1.q(T, i))
                q2 = round(vd2.q(T, j))
                q3 = round(vd3.q(T, k))
                THC1 = round((vd1.THC1(T, i) + vd2.THC1(T, j) + vd3.THC1(T, k)) / T)
                THC2 = round((vd1.THC2(T, i) + vd2.THC2(T, j) + vd3.THC2(T, k)) / T)
                TOC = round((vd1.TOC() + vd2.TOC() + vd3.TOC()) / T)
                TPC2 = round((vd1.TPC2(T, i) + vd2.TPC2(T, j) + vd3.TPC2(T, k)) / T)
                TRC = round((vd1.TRC(T, i) + vd2.TRC(T, j) + vd3.TRC(T, k)) / T)
                TSC1 = round((vd1.TSC1()) / T)
                TSC2 = round((vd1.TSC2() + vd2.TSC2() + vd3.TSC2()) / T)

                TCp = round(THC1 + THC2 + TOC + TPC2 + TRC + TSC1 + TSC2)
                 #điều kiện lọc
                if TCp < mintcp:
                    mintcp = TCp
                    arr1 = np.append(arr1, T)
                    arr1 = np.append(arr1, i)
                    arr1 = np.append(arr1, j)
                    arr1 = np.append(arr1, k)
                    arr1 = np.append(arr1, q1)
                    arr1 = np.append(arr1, q2)
                    arr1 = np.append(arr1, q3)
                    arr1 = np.append(arr1, THC1)
                    arr1 = np.append(arr1, THC2)
                    arr1 = np.append(arr1, TOC)
                    arr1 = np.append(arr1, TPC2)
                    arr1 = np.append(arr1, TRC)
                    arr1 = np.append(arr1, TSC1)
                    arr1 = np.append(arr1, TSC2)
                    arr1 = np.append(arr1, TCp)
                    arr2 = np.append(arr2, TCp)
                # showinfile(T, i, j, k, q1, q2, q3, THC2, THC1, TOC, TPC2, TRC, TSC1, TSC2, TCp)
    arr1 = arr1[-15:]
    y = np.append(y, min(arr2))  # them tcp nhỏ nhất vào mảng trục y
    for i in arr1:
        str1 += str(i) + " : "
    return str1  # trả về chuỗi kết quả


start_time = datetime.now()  # bắt đầu tính h
pr = Parameters()  # khai báo đối tượng thuộc 1 lớp
vd1 = Vendor1()
vd2 = Vendor1()
vd3 = Vendor1()
pr.nhap("para")  # gọi hàm nhập
vd1.nhap(pr, "vendor1")
vd2.nhap(pr, "vendor2")
vd3.nhap(pr, "vendor3")
str1 = ''

for i in range(10, 21):  # vòng lăp chính
    str1 = loop(i)
    print(str1)
    x = np.append(x, i)  # thêm T vào mảng trục x
# end_time = time.time()  # kết thúc bộ đếm h
print('Time elapsed (hh:mm:ss.ms) {}'.format(datetime.now() - start_time))
# ve do thi
plt.plot(x, y, marker=".")
plt.title("do thi toi uu tong chi phi")
plt.show()

