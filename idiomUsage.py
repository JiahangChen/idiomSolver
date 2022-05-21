
from unittest import result
import xlrd
from moviepy.editor import *
import os, sys


def generateIdiomList():
    book = xlrd.open_workbook(".\\idiom.xls")
    sheet = book.sheet_by_index(0)
    resultSet = sheet.col_values(colx=0, start_rowx=0, end_rowx = 18932)
    modifySet = resultSet[:]
    modifySetTmp = []

    a = input("1:")
    b = input("2:")
    c = input("3:")
    d = input("4:")
    for i in a:
        for j in modifySet:
            if i == j[0]:
                modifySetTmp.append(j) 
    modifySet = modifySetTmp
    for i in b:
        modifySetTmp = []
        for j in modifySet:
            if i == j[1]:
                modifySetTmp.append(j) 
    modifySet = modifySetTmp
    for i in c:
        modifySetTmp = []
        for j in modifySet:
            if i == j[2]:
                modifySetTmp.append(j)
    modifySet = modifySetTmp
    for i in d:
        modifySetTmp = []
        for j in modifySet:
            if i == j[3]:
                modifySetTmp.append(j)
    modifySet = modifySetTmp
    for i in modifySet:
        print(i + ", ")



if __name__ == "__main__":
    generateIdiomList()