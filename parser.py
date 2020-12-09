import subprocess as proc
import socket
import sys
import sexpdata


def search(word: str, lst: list):
    for i in range(0,len(lst)):
        if type(lst[i]) is list:
            search(word, lst[i])
        elif lst[i] == word:
            print(word, '=', lst[i+1])

def getValue(word: str, lst: list):
    for i in range(0,len(lst)):
        if type(lst[i]) is list:
            search(word, lst[i])
        elif lst[i] == word:
            return lst[i+1]


# DEBUG SEARCH
# def testSearch(lst: list):
#     #print("list length:", len(lst))
#     for i in range(0, len(lst)):
#         #print(type(lst[i]) is list)
#         if type(lst[i]) is list:
#             testSearch(lst[i])
#         elif lst[i] == 'FieldWidth':
#             print(lst[i+1])
