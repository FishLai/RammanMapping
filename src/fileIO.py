'''
Created on 2018/8/7/

@author: quan_
fd, file directory
filens, file names
FN, Folder name
fPth, file path
nf, new file
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

def exportFile(directory, FileName, WaveNumber, RamanIntensity, floorNum, ceilingNum):
    FN = str(floorNum) +" to "+ str(ceilingNum)
    fPth = os.path.join(directory, FN)
    if not os.path.exists(fPth):
        os.makedirs(fPth)
    fPth = os.path.join(fPth, FileName)
    
    open(fPth, "w+")
    nf = open(fPth, "a+")
    for i in range(len(WaveNumber)-1):
        nf.write(str(WaveNumber[i]) + "\t" + str(RamanIntensity[i]) + "\n")
    return True
    
    
    