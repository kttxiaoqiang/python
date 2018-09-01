
'''
如果是路径就输出路径
继续寻找路径下的文件
如果是文件输出文件名
'''

import os

class PrintPath():
    def __init__(self,spath):
        self._spath=spath

    def print_file_path(self):
        child=os.listdir(self._spath)
        for c in child:
            child_path = os.path.join(self._spath, c)
            if os.path.isdir(child_path):
                print(child_path)
                PrintPath(child_path).print_file_path()
            else:
                print(child_path)



p=PrintPath(spath='')  #此处输入path
p.print_file_path()


