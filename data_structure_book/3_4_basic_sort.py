#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 3.14基本排序算法
@version: 1.0
@Company: CIC
@Author: Li Lanqing
@Contact: 13261903822
@Email: 739772422@qq.com
@LastEditor: Li Lanqing
@Date: 2019-03-12 16:57:30
@LastEditTime: 2019-03-13 08:36:02
'''


def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]


def selectionSort(lyst):
    """
    @Desc: 选择排序
    params lyst: 排序前列表
    return: 排序后列表lyst
    """
    i = 0
    while i < len(lyst) - 1:
        min_index = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            swap(lyst, min_index, i)
        i += 1
    return lyst


def funcname(params):
    """
    @Desc: 
    params params:
    return: 
    """


def main():
    lyst = [5, 8, 4, 6, 2, 9, 3, 11, 10, 1]
    selectionSort(lyst)
    print(lyst)


if __name__ == "__main__":
    main()