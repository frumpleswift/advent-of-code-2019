from vm import Intcode
import numpy as np
from os import system
class Game:
    def __init__(self):
        self.vm = Intcode([int(i) for i in open('arcade-input.txt').read().strip().split(',')],[])
        self.vm.state[0]=2
        self.score=0
        self.blocks=9999
        self.screen=np.full((23,43)," ")
        self.paddle=[-1,-1]
        self.ball=[0,0]
    def _render(self):
        system('clear')
        for layer in self.screen:
            print("".join(p for p in layer))

        #print(self.screen)
        print(self.blocks)
        print(self.score)
        print("ball: ", self.ball, "paddle: ", self.paddle)
    def _paint(self,tile):
        p=' '
        if tile[2] == 4:
            p='o'
            self.ball=[tile[1],tile[0]]
        if tile[2] == 3:
            p='~'
            self.paddle=[tile[1],tile[0]]
        if tile[2] == 2:
            p='+'
        if tile[2] == 1:
            p='#'
        self.screen[tile[1]][tile[0]] = p


    def run(self,moves:list):
        tile=[]
        outs=0
        self.vm.inputs=moves
        while self.blocks > 0 and self.vm.state [ self.vm.pos ] != 99: 
            if self.vm.state[ self.vm.pos ] == 3:
                self._render()
                
                self.vm.inputs=[self.ball[1]-self.paddle[1]]

            t = self.vm.run()
            if t is not None:
                outs+=1
                tile.append(t)
                if len(tile) == 3:
                    if tile[0]==-1 and tile[1] == 0:
                        self.score=tile[2]
                        #self.blocks=sum([1 for x in g.tiles if x[2]==2])
                        self._render()
                    else:
                        tile.append(t)
                        self._paint(tile)
                    tile=[]

#    def play(self,moves:list):

g = Game()
moves=[1 for i in range(0,1000)]
g.run(moves)





