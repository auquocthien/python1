from EOQ import Vendor
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
    n1 = vd1.n(T)
    n2 = vd2.n(T)
    n3 = vd3.n(T)
    q1 = round(vd1.q())
    q2 = round(vd2.q())
    q3 = round(vd3.q())
    TCom = round(vd1.TCom() + vd2.TCom() + vd3.TCom())
    TCH = round(vd1.TCH(T) + vd2.TCH(T) + vd3.TCH(T))
    TCS1 = pr.getA()
    TCD = round(vd1.TCD(T) + vd2.TCD(T) + vd3.TCD(T))
    TCO = round(vd1.TCO() + vd2.TCO() + vd3.TCO())
    TCh = round(vd1.TCh(T) + vd2.TCh(T) + vd3.TCh(T))
    TCS2 = round(vd1.TCS2() + vd2.TCS2() + vd3.TCS2())
    TCP2 = round(vd1.TCP2(T) + vd2.TCP2(T) + vd2.TCP2(T))
    TCp = round((TCom + TCH + TCS1 + TCD + TCO + TCh + TCS2 + TCP2) / T)
    # điều kiện lọc
    if TCp < mintcp:
        mintcp = TCp
        arr1 = np.append(arr1, T)
        arr1 = np.append(arr1, n1)
        arr1 = np.append(arr1, n2)
        arr1 = np.append(arr1, n3)
        arr1 = np.append(arr1, q1)
        arr1 = np.append(arr1, q2)
        arr1 = np.append(arr1, q3)
        arr1 = np.append(arr1, TCom)
        arr1 = np.append(arr1, TCH)
        arr1 = np.append(arr1, TCS1)
        arr1 = np.append(arr1, TCD)
        arr1 = np.append(arr1, TCO)
        arr1 = np.append(arr1, TCh)
        arr1 = np.append(arr1, TCS2)
        arr1 = np.append(arr1, TCP2)
        arr1 = np.append(arr1, TCp)
        arr2 = np.append(arr2, TCp)
        # showinfile(T, i, j, k, q1, q2, q3, THC2, THC1, TOC, TPC2, TRC, TSC1, TSC2, TCp)
    arr1 = arr1[-18:]
    y = np.append(y, min(arr2))  # them tcp nhỏ nhất vào mảng trục y
    for i in arr1:
        str1 += str(i) + " : "
    return str1  # trả về chuỗi kết quả


start_time = datetime.now()  # bắt đầu tính h
pr = Parameters()  # khai báo đối tượng thuộc 1 lớp
vd1 = Vendor()
vd2 = Vendor()
vd3 = Vendor()
pr.nhap("para")  # gọi hàm nhập
vd1.nhap(pr, "vendor1")
vd2.nhap(pr, "vendor2")
vd3.nhap(pr, "vendor3")
str1 = ''

for i in range(10, 46):  # vòng lăp chính
    str1 = loop(i)
    print(str1)
    x = np.append(x, i)  # thêm T vào mảng trục x
# end_time = time.time()  # kết thúc bộ đếm h
print('Time elapsed (hh:mm:ss.ms) {}'.format(datetime.now() - start_time))
# ve do thi
plt.plot(x, y, marker=".")
plt.title("do thi toi uu tong chi phi")
plt.show()

