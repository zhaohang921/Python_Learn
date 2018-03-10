#encoding=utf-8

class B:
    def __init__(self):
        print("B的构造函数被调用")

class A(B):
    def __init__(self,a):
        B.__init__(self)
        self.a=a
    def output(self):
        print(self.a)

    # 静态成员函数
    @staticmethod
    def Doing():
        pass
    @staticmethod
    def AA():
        pass

    #私有成员函数,前面加两个 __
    def __print(self):
       print("test")

if __name__=="__main__":
    b=A(1)
    b.output()
