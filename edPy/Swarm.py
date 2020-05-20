import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata as intGrid
from random import randint

class Particle:
    def __init__(self,position,isdead=False):
        self.XY = np.array(position)
        self.isDed = isdead
        return None
    def whereami(self):
        return self.XY   
    def wheretogo(self,VelField):
        self.v = np.array([float(intGrid(VelField.XY,VelField.Vx,self.XY)),\
                           float(intGrid(VelField.XY,VelField.Vy,self.XY))])
        return self.v
    def move(self,deltaT):
        self.XY = self.XY + self.v*deltaT
        return None
        
        
class Swarm:
    def __init__(self,nombre,size=0):
        self.swarm = list()
        self.X     = list()
        self.Y     = list()
        self.size  = 0
        self.name  = str(nombre)
        return None
    def appendParticle(self,pepa):
        self.swarm.append(pepa)
        self.X.append(pepa.XY[0])
        self.Y.append(pepa.XY[1])
        self.size = len(self.swarm)
        return None
    def moveSwarm(self,VelField,dT):
        for pepa in self.swarm:
            pepa.wheretogo(VelField)
            pepa.move(dT)
        self.refreshXY()
    def refreshXY(self):
        del self.X
        del self.Y
        self.X     = list()
        self.Y     = list()
        for pepa in self.swarm:
            self.X.append(pepa.XY[0])
            self.Y.append(pepa.XY[1])


class Mesh:
    def __init__(self,size):
        #self.X = np.arange(-size,size,10)
        #self.Y = np.arange(-size,size,10)
        #self.poorXY = list()
        #for i in range(len(self.X)):
        #    self.poorXY.append([self.X[i],self.Y[i]])
        #self.XY = np.array(self.poorXY)
        #del self.poorXY
        self.XY = np.array([[-size,-size],[size,-size],[-size,size],[size,size]])
        self.Vx = np.array([5,0,0,-5])
        self.Vy = np.array([0,5,-5,0])
        return None

part1  = Particle(np.array([99,0]),False)
mesh1  = Mesh(150.0)


swarm1 = Swarm(nombre="Holi??")
for t in range(200):
    #if t<11:
    wh = np.array([randint(-99,99),randint(-99,99)])
    #wh = np.array([90.,-90.])
    swarm1.appendParticle(Particle(wh,False))
    swarm1.moveSwarm(mesh1,4)
    plt.scatter(wh[0],wh[1],s=5,c='red',alpha=0.5)
    plt.scatter(swarm1.X,swarm1.Y,s=5,c='blue',alpha=0.1)

plt.ylim(-110,110)
plt.xlim(-110,110)
plt.show()
#print(swarm1.X)