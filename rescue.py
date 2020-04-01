import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra as dj
from random import random
from vm import Intcode
import copy
from os import system
import json

class ASCII:
    def __init__(self):
        self.vm=Intcode([int(i) for i in open('scaffold.txt').read().strip().split(",")],[])



    def snapshot(self):
        while self.vm.state [ self.vm.pos ] != 99:
            pic = self.vm.run()
            if pic is not None:
                return chr(pic)

    def scan(self):
        image=""
        while True:
            pix=self.snapshot()
            if pix is None:
                return image
            image+=pix

themap=ASCII().scan()
print(themap)
ordmap=[ord(c) for c in themap]
scaffold=[]
ordcross=[]
y=0
x=0
i=0

while len(ordmap)>0:
    o = ordmap.pop(0)

    if o == 10:
        print(' ')
        y+=1
        x=0
    else:
        print(chr(o),end='')
        if o == 35:
            scaffold.append([x,y])
        x+=1
    i+=1

alignment=0
intersects=[]

for point in scaffold:
    try:
        i = scaffold.index([point[0],point[1]+1])
        try:
            i = scaffold.index([point[0],point[1]-1])
            try:
                i = scaffold.index([point[0]+1,point[1]])
                try:
                    i = scaffold.index([point[0]-1,point[1]])
                    intersects.append(point)
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass

print(sorted(intersects))

ordmap=[ord(c) for c in themap]

y=0
x=0

print(" 01234567890123456789012345678901234567890123456789")
print(y%10,end='')

while len(ordmap)>0:
    o = ordmap.pop(0)
    if o == 10:
        print(' ')
        y+=1
        print(y%10,end='')
        x=0
    else:

        if o == 35:
            try:
                intersects.index([x,y])
                print("O",end='')
            except:
                print("#",end='')
        else:
            print(chr(o),end='')
        x+=1
    i+=1
print("################################################")
align=0
for p in intersects:
    align+=p[0]*p[1]
print(align)
