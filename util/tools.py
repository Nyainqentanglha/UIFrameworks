#encoding:utf-8
__author__ = 'yongzhang'


def getMaxDict(listDicts):
    maxSize = listDicts[0]
    for index in range(1,len(listDicts)):
        if listDicts[index]['width'] > maxSize['width'] or listDicts[index]['height'] > maxSize['height']:
            maxSize = listDicts[index]
    return maxSize