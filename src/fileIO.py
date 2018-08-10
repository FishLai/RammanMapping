'''
Created on 2018年8月7日

@author: quan_
fd, file directory
filens, file names
FN, Folder name
'''

import os



def pichFile(directory):
    fd = []
    filens = []
    isInfo = 0
    for Path, dirs, fns in os.walk(directory):
        for fn in fns:
            if isInfo == 0 and "Info" in fn:
                isInfo = 1
                continue
            filens.append(fn)
            filePth = os.path.join(Path, fn)
            fd.append(filePth)
    return fd, filens

def exportFile(FileName, WaveNumber, RamanIntensity, floorNum, ceilingNum):
    FN = floorNum +" to "+ ceilingNum
    