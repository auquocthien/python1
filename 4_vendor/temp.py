from EOQ import Vendor
from Parameters import Parameters

pr = Parameters()
vd1 = Vendor()
pr.nhap("para")
vd1.nhap(pr, "vendor3")
for i in range(1, 10000):
    if vd1.new_q(i) % 10 == 0:
        print(vd1.new_q(i), i)
