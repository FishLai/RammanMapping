'''
Created on 2018年8月6日

@author: quan_
WN means wave number, RI: Raman Intensity
'''
import numpy as np
import math
#use numpy.genfromtxt could choose range
def divideData(directory, wnFloor, wnCeiling, IF = None, IC = None):
    if IF == None and IC == None:
        x_i, y_i = np.genfromtxt(directory, skip_header = 200, skip_footer = 530, unpack = True)       
        for i in range(x_i.size):
            if math.floor(x_i[i]) == wnFloor:
                index_floor = i
                print(index_floor)
                break
        for i in range(x_i.size):
            if math.floor(x_i[i]) == wnCeiling:
                index_ceiling = i+1
                print(index_ceiling)
                break
        WN = x_i[index_floor : index_ceiling]
        RI = y_i[index_floor : index_ceiling]
    if isinstance(IF, int) and isinstance(IC, int):
        index_floor = IF
        index_ceiling = IC
        x_i, y_i = np.genfromtxt(directory, skip_header = 200, skip_footer = 530, unpack = True)
        WN = x_i[index_floor : index_ceiling]
        RI = y_i[index_floor : index_ceiling]
        
    return WN, RI, index_floor, index_ceiling


if __name__ == '__main__':
    x, y, i_f, i_c = divideData("D:/Users/pc/Downloads/FishLai/Temp/test_ramanMapping/test-z7.9168y37.5310x44.7104.txt", 200, 250)
    print(x, i_f, i_c)