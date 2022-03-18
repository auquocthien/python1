class Parameters:
    __A = 0
    __Cps = 0  # xe tai nho
    __Cpm = 0  # xe tai trung binh
    __Cpb = 0  # xe tai nang
    __Cs = 0
    __Cm = 0
    __Cb = 0

    def __init__(self):
        self.__A = 0
        self.__Cps = 0
        self.__Cpm = 0
        self.__Cpb = 0
        self.__Cs = 0
        self.__Cm = 0
        self.__Cb = 0

    def copy(self, para):
        self.__A = para.__A
        self.__Cps = para.__Cps
        self.__Cpm = para.__Cpm
        self.__Cpb = para.__Cpb
        self.__Cs = para.__Cs
        self.__Cm = para.__Cm
        self.__Cb = para.__Cb

    def nhap(self, fileName):
        f = open("data/{}.txt".format(fileName), "r")
        str1 = f.readline()
        self.__A = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cps = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cpm = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cpb = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cs = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cm = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cb = int(str1[str1.rfind(' ') + 1:])

    def hienthi(self):
        print("A: {}, Cps: {}, Cpm: {}, Cpb: {}, Cs: {}, Cm: {}, Cb: {}".format(
            self.__A, self.__Cps, self.__Cpm, self.__Cpb, self.__Cs, self.__Cm, self.__Cb))

    def getA(self):
        return self.__A

    def getCps(self):
        return self.__Cps

    def getCpm(self):
        return self.__Cpm

    def getCpb(self):
        return self.__Cpb

    def getCs(self):
        return self.__Cs

    def getCm(self):
        return self.__Cm

    def getCb(self):
        return self.__Cb
