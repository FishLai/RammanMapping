'''
Created on 2018/8/10/

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
    filedirs, filens = fileIO.pichFile(directory)
    print(len(filedirs))
    for i in range(len(filedirs)):
        wn, ri, I_F, I_C = dividData.divideData(filedirs[i], wnFloor, wnCeiling, I_F, I_C)
        fileIO.exportFile(directory, filens[i], wn, ri, wnFloor, wnCeiling)
    return True