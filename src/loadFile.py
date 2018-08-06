'''
Created on 2018年8月6日

@author: quan_
'''
import numpy as np
#use numpy.genfromtxt could choose range
def loadFile(directory, floor, ceiling):
    x, y = np.genfromtxt(directory, skip_header = floor, skip_footer = ceiling, unpack = True)
    return x, y
if __name__ == '__main__':
    x, y = loadFile("C:/workspace/Data/test_ramanMapping/test-z7.9168y37.5310x44.7104.txt", 0, 0)
    print(x)