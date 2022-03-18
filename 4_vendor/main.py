from VMI import Vendor
from Parameters import Parameters
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def some_thing(str, arr, list, x, y):
    a = int(str[list[x]:list[y]])
    arr = np.append(arr, a)
    return arr


# ghi du lieu vao file txt


def showinfile(T, i, j, k, L, q1, q2, q3, q4, TCH, TCh, TCO, TCP2, TCD, TCS1, TCS2, TCp):
    f = open("dataoutVMI/loop %s.txt" % T, "a")  # tạo file txt ứng với mỗi vòng lặp
    str1 = ''  # khai báo chuỗi rỗng
    arr = np.array([T, i, j, k, L, q1, q2, q3, q4, TCH, TCh, TCO, TCP2, TCD, TCS1, TCS2, TCp])  # khai báo mảng
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
                for L in range(1, T + 1):
                    q1 = round(vd1.q(T, i))
                    q2 = round(vd2.q(T, j))
                    q3 = round(vd3.q(T, k))
                    q4 = round(vd4.q(T, L))
                    TCH = round((vd1.TCH(T, i) + vd2.TCH(T, j) + vd3.TCH(T, k) + vd4.TCH(T, L)) / T)
                    TCh = round((vd1.TCh(T, i) + vd2.TCh(T, j) + vd3.TCh(T, k) + vd4.TCh(T, L)) / T)
                    TCO = round((vd1.TCO() + vd2.TCO() + vd3.TCO() + vd4.TCO()) / T)
                    TCP2 = round((vd1.TCP2(T, i) + vd2.TCP2(T, j) + vd3.TCP2(T, k) + vd4.TCP2(T, L)) / T)
                    TCD = round((vd1.TCD(T, i) + vd2.TCD(T, j) + vd3.TCD(T, k) + vd4.TCD(T, L)) / T)
                    TCS1 = round(pr.getA() / T)
                    TCS2 = round((vd1.TCS2() + vd2.TCS2() + vd3.TCS2() + vd4.TCS2()) / T)
                    TCp = round(TCH + TCh + TCO + TCP2 + TCD + TCS1 + TCS2)
                    # điều kiện lọc
                    if TCp < mintcp:
                        mintcp = TCp
                        arr1 = np.append(arr1, T)
                        arr1 = np.append(arr1, i)
                        arr1 = np.append(arr1, j)
                        arr1 = np.append(arr1, k)
                        arr1 = np.append(arr1, L)
                        arr1 = np.append(arr1, q1)
                        arr1 = np.append(arr1, q2)
                        arr1 = np.append(arr1, q3)
                        arr1 = np.append(arr1, q4)
                        arr1 = np.append(arr1, TCH)
                        arr1 = np.append(arr1, TCh)
                        arr1 = np.append(arr1, TCO)
                        arr1 = np.append(arr1, TCP2)
                        arr1 = np.append(arr1, TCD)
                        arr1 = np.append(arr1, TCS1)
                        arr1 = np.append(arr1, TCS2)
                        arr1 = np.append(arr1, TCp)
                        arr2 = np.append(arr2, TCp)
                        # showinfile(T, i, j, k, L, q1, q2, q3, q4, TCh, TCH, TCO, TCP2, TCD, TCS1, TCS2, TCp)
    arr1 = arr1[-17:]
    y = np.append(y, min(arr2))  # them tcp nhỏ nhất vào mảng trục y
    for i in arr1:
        str1 += str(i) + " : "
    return str1  # trả về chuỗi kết quả


start_time = datetime.now()  # bắt đầu tính h
pr = Parameters()  # khai báo đối tượng thuộc 1 lớp
vd1 = Vendor()
vd2 = Vendor()
vd3 = Vendor()
vd4 = Vendor()
pr.nhap("para")  # gọi hàm nhập
vd1.nhap(pr, "Vendor1")
vd2.nhap(pr, "vendor2")
vd3.nhap(pr, "vendor3")
vd4.nhap(pr, "vendor4")
pr.hienthi()
vd1.hienthi()
vd2.hienthi()
vd3.hienthi()
vd4.hienthi()
str1 = ''

best_result = 9999999
str_result = ''

TCH = np.array([], dtype='i')
TCh = np.array([], dtype='i')
TCO = np.array([], dtype='i')
TCP2 = np.array([], dtype='i')
TCD = np.array([], dtype='i')
TCS1 = np.array([], dtype='i')
TCS2 = np.array([], dtype='i')

for i in range(10, 45):  # vòng lăp chính
    str1 = loop(i)
    str1 = str1.strip()
    str1 = str1[:-2]
    index = str1.rfind(" ")
    to_find = ' '
    list1 = [i for i, x in enumerate(str1) if x == to_find]

    if int(str1[index:]) < best_result:
        best_result = int(str1[index:])
        str_result = str1[:list1[8]]

    TCH = some_thing(str1, TCH, list1, 17, 18)
    TCh = some_thing(str1, TCh, list1, 19, 20)
    TCO = some_thing(str1, TCO, list1, 21, 22)
    TCP2 = some_thing(str1, TCP2, list1, 23, 24)
    TCD = some_thing(str1, TCD, list1, 25, 26)
    TCS1 = some_thing(str1, TCS1, list1, 27, 28)
    TCS2 = some_thing(str1, TCS2, list1, 29, 30)

    print(str1)
    x = np.append(x, i)  # thêm T vào mảng trục x
print("best result: {}\ntcp: {}".format(str_result, best_result))
# end_time = time.time()  # kết thúc bộ đếm h
print('Time elapsed (hh:mm:ss.ms) {}'.format(datetime.now() - start_time))
# ve do thi
plt.plot(x, y, marker=".")
plt.title("do thi toi uu tong chi phi")
plt.show()

plt.plot(x, TCH)
plt.plot(x, TCh)
plt.plot(x, TCO)
plt.plot(x, TCP2)
plt.plot(x, TCD)
plt.plot(x, TCS1)
plt.plot(x, TCS2)
plt.show()
