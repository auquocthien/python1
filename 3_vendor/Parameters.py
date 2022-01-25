class Parameters:
    __A = 0
    __Cps = 0
    __Cpm = 0
    __Cs = 0
    __Cm = 0

    def __init__(self):
        __A = 0
        __Cps = 0
        __Cpm = 0
        __Cs = 0
        __Cm = 0

    def copy(self, para):
        self.__A = para.__A
        self.__Cps = para.__Cps
        self.__Cpm = para.__Cpm
        self.__Cs = para.__Cs
        self.__Cm = para.__Cm

    def nhap(self, fileName):
        f = open("data/{}.txt".format(fileName), "r")
        str1 = f.readline()
        self.__A = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cps = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cpm = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cs = int(str1[str1.rfind(' ') + 1:])
        str1 = f.readline()
        self.__Cm = int(str1[str1.rfind(' ') + 1:])

    def hienthi(self):
        print("A: {}, Cps:{}, Cpm:{}, Cs:{}, Cm:{}".format(self.__A, self.__Cps, self.__Cpm, self.__Cs, self.__Cm))

    def getA(self):
        return self.__A

    def getCps(self):
        return self.__Cps

    def getCpm(self):
        return self.__Cpm

    def getCs(self):
        return self.__Cs

    def getCm(self):
        return self.__Cm
