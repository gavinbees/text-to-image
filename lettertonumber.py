from PIL import Image
import numpy as np
import math
rgbs = []

def file_to_string(textfile):
    with open(textfile, encoding="utf8") as f:
        data = f.readlines()
    s = ""
    for x in data:
        for y in x:
            s+=y
    print(len(s))
    return s
            


def string_to_numbers(original):
    s = "" #alphanumeric string
    n = "" #numberfied string
    for x in original.lower():
        if x.isalpha():
            s+=x
    for i in range(len(s)):
        val = ord(s[i]) - 96 #makes a = 1, b = 2 etc
        n = n + str(val)
    while len(n) % 9 !=0:
        n = n[:-1]
    return n


def rgb_array(n):
    rgb = ""
    for x in n:
        rgb+=x
        if len(rgb) == 3:
            if int(rgb) > 255: #a number like 300, outside of rgb range, is converted to 03, 00
                rgb = ("0" + str(rgb))[:-1] 
            rgbs.append(int(rgb))
            rgb = ""

def resize_arr():
    goal = int(math.pow(int(math.sqrt(len(rgbs)/3)),2)*3) # crop to a square
    while len(rgbs) != goal:
        rgbs.pop(len(rgbs)-1)
    return int(math.sqrt(len(rgbs)/3))

def create_nparr(dimension):
    nparr = []
    z = 0
    for x in range(dimension): 
        row = []
        for y in range(dimension):
            row.append(tuple(rgbs[z:z+3]))
            z+=3
        nparr.append(row)
    nparr = np.array(nparr, dtype=np.uint8)  
    return nparr 

rgb_array(string_to_numbers(file_to_string('put_file_here.txt'))) #put a text file here
dim = resize_arr()
nparr = create_nparr(dim)
img = Image.fromarray(nparr, 'RGB')
img.show()


