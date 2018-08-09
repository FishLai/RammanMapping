'''
Created on 2018年8月7日

@author: quan_
'''
import os



def pichFile(directory):
    f = []
    isInfo = 0
    for Path, dirs, fns in os.walk(directory):
        for fn in fns:
            if isInfo == 0 and "Info" in fn:
                isInfo = 1
                continue
            filePth = os.path.join(Path, fn)
            f.append(filePth)
    return f

def exportFile():
    pass