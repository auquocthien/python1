from Parameters import Parameters
import math as math


class Vendor:
    __pr = Parameters()
    __D = 0
    __h = 0
    __pi = 0
    __s = 0
    __H = 0
    __U = 0
    __Om = 0
    __x = 0
    __O = 0

    def __init__(self):
        self.__D = 0
        self.__h = 0
        self.__pi = 0
        self.__s = 0
        self.__H = 0
        self.__U = 0
        self.__Om = 0
        self.__x = 0
        self.__O = 0

    def nhap(self, pra, fileName):
        self.__pr.copy(pra)
        f = open("dataEOQ/{}.txt".format(fileName), "r")
        str1 = f.readline()
        self.__D = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__h = float(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__pi = float(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__H = float(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__U = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Om = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__x = int(str1[str1.rfind(' ') + 1:])
        if self.__x == 0:
            str1 = f.readline()
            self.__s = int(str1[str1.rfind(' ') + 1:])
        elif self.__x == 1:
            str1 = f.readline()
            self.__O = int(str1[str1.rfind(' ') + 1:])

    def hienthi(self):
        if self.__x == 1:
            print("D:{}, h:{}, pi:{}, O:{}, H:{}, U:{}, Om:{}, x:{}".format(
                self.__D, self.__h, self.__pi, self.__O, self.__H, self.__U,self.__Om, self.__x))
        elif self.__x == 0:
            print("D:{}, h:{}, pi:{}, s:{}, H:{}, U:{}, Om:{}, x:{}".format(
                self.__D, self.__h, self.__pi, self.__s, self.__H, self.__U,self.__Om, self.__x))

    def q(self):
        return round(math.sqrt((2 * self.__Om * self.__D) / self.__H))

    def new_q(self, D):
        return round(math.sqrt((2 * self.__Om * D) / self.__H))

    def n(self, T):
        return round((self.__D * T) / self.q())

    def TCom(self):
        return (self.__Om * self.__D) / self.q()

    def TCH(self, T):
        return (self.__H * self.q() * T) / 2

    def TCS1(self):
        return self.__pr.getA()

    # def TCD(self, i):
    #     cpm = self.__pr.getCpm()
    #     cps = self.__pr.getCps()
    #     cpb = self.__pr.getCpb()
    #     cm = self.__pr.getCm()
    #     cs = self.__pr.getCs()
    #     cb = self.__pr.getCb()
    #     qi = self.q()
    #     tci = 0
    #     r1 = qi % cpb
    #     r2 = qi % cpm
    #     if qi >= cpb:
    #         if 0 < r1 < cps:
    #             tci = (qi // cpb) * cb + cs
    #         if cps < r1 <= 2 * cps:
    #             tci = (qi // cpb) * cb + 2 * cs
    #         if 2 * cps < r1 < cpm:
    #             tci = (qi // cpb) * cb + cm
    #         if cpm < r1 <= 2 * cpm:
    #             tci = (qi // cpb) * cb + 2 * cm
    #         if r1 == 0:
    #             tci = (qi // cpb) * cb
    #         if r1 > 2 * cpm:
    #             tci = (qi // cpb) * cb + cb
    #     elif 0 <= qi < cpb:
    #         if 2 * cps < r2 <= cpm:
    #             tci = (qi // cpm) * cm + cm
    #         if cps < r2 <= 2 * cps:
    #             tci = (qi // cpm) * cm + 2 * cs
    #         if 0 < r2 <= cps:
    #             tci = (qi // cpm) * cm + cs
    #         if r2 == 0:
    #             tci = cm
    #     return i * tci

    def TCD(self, ni):
        cpm = self.__pr.getCpm()
        cps = self.__pr.getCps()
        cpb = self.__pr.getCpb()
        cm = self.__pr.getCm()
        cs = self.__pr.getCs()
        cb = self.__pr.getCb()
        qi = self.q()
        tci = 0
        r1 = qi % cpb
        r2 = qi % cpm
        if qi > 2 * cpm:
            if 0 < r1 <= cps:
                tci = (qi // cpb) * cb + cs
            if cps < r1 <= (2 * cps):
                tci = (qi // cpb) * cb + 2 * cs
            if (2 * cps) < r1 <= cpm:
                tci = (qi // cpb) * cb + cm
            if cpm < r1 <= (cpm + cps):
                tci = (qi // cpb) * cb + cm + cs
            if (cpm + cps) < r1 <= (cpm + 2 * cps):
                tci = (qi // cpb) * cb + cm + 2 * cs
            if (cpm + 2 * cps) < r1 <= (2 * cpm):
                tci = (qi // cpb) * cb + 2 * cm
            if r1 == 0:
                tci = (qi // cpb) * cb
            if (2 * cpm) < r1 < cpb:
                tci = (qi // cpb) * cb + cb
        elif 0 <= qi <= (2 * cpm):
            if 2 * cps < r2 <= cpm:
                tci = (qi // cpm) * cm + cm
            if cps < r2 <= (2 * cps):
                tci = (qi // cpm) * cm + 2 * cs
            if 0 < r2 <= cps:
                tci = (qi // cpm) * cm + cs
            if r2 == 0:
                tci = cm
        return ni * tci

    def Q(self):
        if self.__x == 1:
            return math.sqrt((2 * self.__O * self.__D) / self.__h)
        else:
            return self.q()

    def TCO(self):
        return (self.__O * self.__D * self.__x) / self.Q()

    def TCh(self, T):
        tch1 = (self.__h * self.Q() * T * self.__x) / 2
        tch2 = (self.__h * self.q() * T * (1 - self.__x)) / 2
        return tch1 + tch2

    def TCS2(self):
        return self.__s * (1 - self.__x)

    def TCP2(self, T):
        a = 0
        if self.q() <= self.__U:
            return int(a)
        elif self.q() > self.__U:
            return (self.n(T) * ((self.q() - self.__U) * (self.q() - self.__U)) * self.__pi) / (2 * self.__D)
