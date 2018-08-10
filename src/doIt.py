'''
Created on 2018年8月10日

@author: pc
filedirs, files' dorectories; filedir, file's directory
filens, file names, 
'''
import dividData, fileIO

def doIt(parameters):
    wnFloor = parameters[0]
    wnCeiling = parameters[1]
    directory = parameters[2]
    
    I_F = None
    I_C = None
    for filedirs, filens in fileIO.pichFile(directory):
        for filedir, filen in filedirs, filens:
            wn, ri, I_F, I_C = dividData.divideData(filedir, wnFloor, wnCeiling, I_F, I_C)
            fileIO.exportFile(filen, wn, ri)
    return True