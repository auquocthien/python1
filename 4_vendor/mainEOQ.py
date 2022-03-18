from EOQ import Vendor
from Parameters import Parameters
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


# ghi du lieu vao file txt
def showinfile(T, n1, n2, n3, n4, q1, q2, q3, q4, TCom, TCH, TCS1, TCD, TCO, TCh, TCS2, TCP2, TCp):
    f = open("dataoutEOQ/loop %s.txt" % T, "a")  # tạo file txt ứng với mỗi vòng lặp
    str1 = ''  # khai báo chuỗi rỗng
    arr = np.array([T, n1, n2, n3, n4, q1, q2, q3, q4, TCom, TCH, TCS1, TCD, TCO, TCh, TCS2, TCP2, TCp])  # khai báo mảng
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
    n1 = vd1.n(T)
    n2 = vd2.n(T)
    n3 = vd3.n(T)
    n4 = vd4.n(T)
    q1 = round(vd1.q())
    q2 = round(vd2.q())
    q3 = round(vd3.q())
    q4 = round(vd4.q())
    TCom = round(vd1.TCom() + vd2.TCom() + vd3.TCom() + vd4.TCom())
    TCH = round(vd1.TCH(T) + vd2.TCH(T) + vd3.TCH(T) + vd4.TCH(T))
    TCS1 = pr.getA()
    # tcd1 = vd1.TCD(n1)
    # tcd2 = vd2.TCD(n2)
    # tcd3 = vd3.TCD(n3)
    # tcd4 = vd4.TCD(n4)
    # TCD = tcd1 + tcd2 + tcd3 + tcd4
    TCD = round(vd1.TCD(n1) + vd2.TCD(n2) + vd3.TCD(n3) + vd4.TCD(n4))
    TCO = round(vd1.TCO() + vd2.TCO() + vd3.TCO() + vd4.TCO())
    TCh = round(vd1.TCh(T) + vd2.TCh(T) + vd3.TCh(T) + vd4.TCh(T))
    TCS2 = round(vd1.TCS2() + vd2.TCS2() + vd3.TCS2() + vd4.TCS2())
    TCP2 = round(vd1.TCP2(T) + vd2.TCP2(T) + vd3.TCP2(T) + vd4.TCP2(T))
    TCp = round((TCom + TCH + TCS1 + TCD + TCO + TCh + TCS2 + TCP2) / T)
    # điều kiện lọc
    arr1 = np.append(arr1, T)
    arr1 = np.append(arr1, n1)
    arr1 = np.append(arr1, n2)
    arr1 = np.append(arr1, n3)
    arr1 = np.append(arr1, n4)
    arr1 = np.append(arr1, q1)
    arr1 = np.append(arr1, q2)
    arr1 = np.append(arr1, q3)
    arr1 = np.append(arr1, q4)
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
    showinfile(T, n1, n2, n3, n4, q1, q2, q3, q4, TCom, TCH, TCS1, TCD, TCO, TCh, TCS2, TCP2, TCp)
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
vd4 = Vendor()
pr.nhap("para")  # gọi hàm nhập
vd1.nhap(pr, "vendor1")
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

for i in range(10, 45):  # vòng lăp chính
    str1 = loop(i)
    str1 = str1.strip()
    str1 = str1[:-2]
    index = str1.rfind(' ')
    to_find = ' '
    list1 = [i for i, x in enumerate(str1) if x == to_find]
    if int(str1[index:]) < best_result:
        best_result = int(str1[index:])
        str_result = str1[:list1[8]]
    print(str1)
    x = np.append(x, i)  # thêm T vào mảng trục x
# end_time = time.time()  # kết thúc bộ đếm h
print("best result: {}\ntcp: {}".format(str_result, best_result))
print('Time elapsed (hh:mm:ss.ms) {}'.format(datetime.now() - start_time))
# ve do thi
plt.plot(x, y, marker=".")
plt.title("do thi toi uu tong chi phi")
plt.show()

