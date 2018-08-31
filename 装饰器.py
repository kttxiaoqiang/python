# import time
# def printTime(f):
#     def wrapper(*args,**kwargs):
#         print("Time:",time.ctime())
#         return f(*args,**kwargs)
#     return wrapper
#
# @printTime
# def hello():
#     print('hello world')
#
# hello()
#
#
# @printTime
# def hello2():
#     print("今天是星期五")
#     print("这里很多选择")
#
# hello2()
# print("*"*50)
#
# def hello3():
#     print("woshi hello3")
#     print("hhh")
#
# printTime(hello3())


#设计一个装饰器记录函数执行总时间(在不改变原方法的情况下)
'''
import time
def func():
    print("hello")
    time.sleep(5)
    print("world")
'''
import time
def timediff(f):                  #装饰器写法基本固定 以函数作为装饰器中的参数来执行
    def wrapper(*args,**kwargs):
        starttime=time.time()
        f(*args,**kwargs)
        endtime=time.time()
        time_diff=endtime-starttime
        print('运行总时间是：',time_diff)
        return time_diff
    return wrapper


@timediff
def func():
    print("hello")
    time.sleep(5)
    print("world")
func()