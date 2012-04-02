import json
import random

def gol(data):
    """This is the function that the cgi script calls."""
    gen = json.loads(data)
    if not gen:
        gen = randomStart() 
    nextGen = GOL(gen).getNextGen()
    data = json.dumps(nextGen)
    return data

def randomStart():
    points = []
    for i in range(180, 220, 5):
        for j in range(175, 225, 5):
            rand = random.random()
            if (rand > 0.5):
                point = [i, j]
                points.append(point)
    return points

glider = [[20, 20], [20, 25], [20, 30], [15, 30], [10, 25]]

class GOL():
    def __init__(self, gen):
        self.gen = gen

    def getNextGen(self):
        nextGen = []
        for i, coord in enumerate(self.gen):
            numNeighbours = self.countNeighbours(i, coord)
            if numNeighbours == 2 or numNeighbours == 3:
                if not self.contains(nextGen, coord):
                    nextGen.append(coord)
            self.birthAdjacents(i, coord, nextGen)
        return nextGen
    
    def birthAdjacents(self, n, coords, nextGen):
        adjacents = self.getAdjacents(coords)
        for adj in adjacents: 
            if self.countNeighbours(-1, adj) == 3:
                if not self.contains(nextGen, adj) :
                    nextGen.append(adj)
                    
    def contains(self, arr, coord):
        for c in arr:
            if c[0] == coord[0] and c[1] == coord[1]:
                return True
        return False
    
    def getAdjacents(self, coords):
        adjs = []
        myX = coords[0]
        myY = coords[1]
        adjs.append([myX, myY+5])
        adjs.append([myX+5, myY+5])
        adjs.append([myX+5, myY])
        adjs.append([myX+5, myY-5])
        adjs.append([myX, myY-5])
        adjs.append([myX-5, myY-5])
        adjs.append([myX-5, myY])
        adjs.append([myX-5, myY+5])
        return adjs
    
    def countNeighbours(self, n, coords):
        count = 0
        for i in range(len(self.gen)):
            if i != n:
                if self.isNextTo(coords, self.gen[i]):
                    count += 1
        return count
    
    def isNextTo(self, a, b):
       next = True
       next = next and abs(a[0] - b[0]) <= 5
       next = next and abs(a[1] - b[1]) <= 5
       return next
   
import unittest
class TestGol(unittest.TestCase):
    def testGetNextGen(self):
        gliderStepTwo = [[25, 25], [15, 20], [20, 25], [20, 30], [15, 30]]
        self.assertEquals(gliderStepTwo, GOL(glider).getNextGen())
    
    def testCountNeighbours(self):
        gen = [[0, 0], [0, 5], [5, 5], [20, 0]]
        gol = GOL(gen)
        self.assertEquals(2, gol.countNeighbours(1, [0, 5]))

if __name__ == '__main__':
    unittest.main()
