'''
Created on 2018年8月6日

@author: quan_
WN means wave number, RI: Raman Intensity
'''
import numpy as np
import math
#use numpy.genfromtxt could choose range
def divideData(directory, wnFloor, wnCeiling):
    x_i, y_i = np.genfromtxt(directory, skip_header = 200, skip_footer = 530, unpack = True)
    for i in range(x_i.size):
        if math.floor(x_i[i]) == wnFloor:
            index_floor = i
            break
    for i in range(x_i.size):
        if math.floor(x_i[i]) == wnCeiling:
            index_ceiling = i+1
            break
    WN = x_i[index_floor : index_ceiling]
    RI = y_i[index_floor : index_ceiling]
    return WN, RI, index_floor, index_ceiling

if __name__ == '__main__':
    x, y, i_f, i_c = divideData("C:/workspace/Data/test_ramanMapping/test-z7.9168y37.5310x44.7104.txt", 200, 250)
    print(x)