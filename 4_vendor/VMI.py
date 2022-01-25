from Parameters import Parameters


class Vendor:
    __pr = Parameters()
    __D = 0
    __bv = 0.0
    __pi = 0.0
    __a = 0
    __H = 0.0
    __O = 0
    __U = 0
    __x = 0

    def __init__(self):
        self.__D = 0
        self.__bv = 0
        self.__pi = 0
        self.__a = 0
        self.__H = 0
        self.__O = 0
        self.__U = 0
        self.__x = 0

    def copy(self, vd):
        self.__D = vd.__D
        self.__bv = vd.__bv
        self.__pi = vd.__pi
        self.__a = vd.__a
        self.__H = vd.__H
        self.__O = vd.__O
        self.__U = vd.__U
        self.__x = vd.__x

    def nhap(self, pra, fileName):
        self.__pr.copy(pra)
        f1 = open("data/{}.txt".format(fileName), "r")
        str1 = f1.readline()
        self.__D = int(str1[str1.rfind(' ') + 1:])
        str1 = f1.readline()
        self.__bv = float(str1[str1.rfind(' ') + 1:])
        str1 = f1.readline()
        self.__pi = float(str1[str1.rfind(' ') + 1:])
        str1 = f1.readline()
        self.__H = float(str1[str1.rfind(' ') + 1:])
        str1 = f1.readline()
        self.__U = int(str1[str1.rfind(' ') + 1:])
        str1 = f1.readline()
        self.__x = int(str1[str1.rfind(' ') + 1:])
        if self.__x == 0:
            str1 = f1.readline()
            self.__a = int(str1[str1.rfind(' ') + 1:])
        elif self.__x == 1:
            str1 = f1.readline()
            self.__O = int(str1[str1.rfind(' ') + 1:])

    def hienthi(self):
        if self.__x == 0:
            print("D:{}, bv:{}, pi:{}, a:{}, H:{}, U:{}".format(self.__D, self.__bv, self.__pi, self.__a, self.__H, self.__U))
        elif self.__x == 1:
            print("D:{}, bv:{}, pi:{}, O:{}, H:{}, U:{}".format(self.__D, self.__bv, self.__pi, self.__O, self.__H, self.__U))

    @staticmethod
    def ti(T, i):
        return T/i

    def q(self, T, i):
        return self.ti(T, i) * self.__D

    def THC1(self, T, i):
        return (self.__H * self.q(T, i) * T)/2

    def TSC1(self):
        return self.__pr.getA()

    def TOC(self):
        return self.__O * self.__x

    def TSC2(self):
        return self.__a * (1 - self.__x)

    def THC2(self, T, i):
        I = (self.q(T, i)*(i-1))/2
        THC21 = ((self.__bv*self.q(T, i)*T)/2)*(1-self.__x)
        THC22 = self.__bv*I*T*self.__x
        return THC21+THC22

    def TPC2(self, T, i):
        a = 0
        if self.q(T, i) <= self.__U:
            return int(a)
        elif self.q(T, i) > self.__U:
            return (i * ((self.q(T, i) - self.__U) * (self.q(T, i) - self.__U)) * self.__pi) / (2 * self.__D)

    def TRC(self, T, i):
        cpm = self.__pr.getCpm()
        cps = self.__pr.getCps()
        cpb = self.__pr.getCpb()
        cm = self.__pr.getCm()
        cs = self.__pr.getCs()
        cb = self.__pr.getCb()
        qi = self.q(T, i)
        tci = 0
        r1 = qi % cpb
        r2 = qi % cpm
        d1 = qi // cpb
        d2 = qi // cpm
        if qi >= cps:
            if 0 < r1 < cps:
                tci = d1 * cb + cs
            if cps < r1 <= 2 * cps:
                tci = d1 * cb + 2 * cs
            if 2 * cps < r1 < cpm:
                tci = d1 * cb + cm
            if cpm < r1 <= 2 * cpm:
                tci = d1 * cb + 2 * cm
            if r1 == 0:
                tci = d1 * cb
            if r1 > 2 * cpm:
                tci = d1 * cb + cb
        elif 0 <= qi < cpb:
            if 2 * cps < r2:
                tci = d2 * cm + cm
            if cps < r2 <= 2 * cps:
                tci = d2 * cm + 2 * cs
            if 0 < r2 <= cps:
                tci = d2 * cm + cs
            if r2 == 0:
                tci = cm
        return i*tci
