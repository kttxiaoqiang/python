#作业：
# 1.在用户输入年龄的时候可以输入整数、小数、浮点数
# 2.但是为了内部数据清洁，我们统一保存整数，直接舍去小数点。
class Age():
    def __init__(self):
        self._age='请输入年龄：'

    def fget(self):
        return self._age

    def fset(self,value):
        if isinstance(value,int):
            print('输入的整数')
            self._age=value
        else:
            print('输入的是小数')
            self._age=int(value)
    def fdel(self):
        pass

    x=property(fget,fset,fdel,'清洁内部数据取整')

if __name__=='__main__':
    a=Age()
    a.x =10
    print(a.x)
    print("*"*50)
    a.x=21.1111111111111111111
    print(a.x)