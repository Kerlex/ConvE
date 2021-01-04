#%%
import numpy as np
import matplotlib.pyplot as plt
import os


class methodData():
    """
    class to encompise the data of a single method
    """
    def __init__(self, path):
        self.hits1 = []
        self.hits5 = []
        self.hits10 = []
        self.mrr = []
        self.path = path
    
    def add2hits1(self,messur):
        self.hits1.append(messur)

    def add2hits5(self,messur):
        self.hits5.append(messur)
        
    def add2hits10(self,messur):
        self.hits10.append(messur)
    
    def add2mrr(self,messur):
        self.mrr.append(messur)

    def getHits1(self):
        return np.array(self.hits1)

    def getHits5(self):
        return np.array(self.hits5)
    
    def getHits10(self):
        return np.array(self.hits10)

    def getMrr(self):
        return np.array(self.mrr)

    def readpath(self):
        N = 0
        with open(self.path,'r') as File:
            for N, line in enumerate(File):
                if N%18 == 14: 
                    self.add2hits1(float(line.split()[-1]))
                if N%18 == 15: 
                    self.add2hits5(float(line.split()[-1]))
                if N%18 == 16: 
                    self.add2hits10((float(line.split()[-1])))
                if N%18 == 17: 
                    self.add2mrr(float(line.split()[-1]))


class plotter():
    def __init__(self,*args):
        self.data = args
        self.N = len(args)
        self.labels = []
        self.Xlabel = ""
        self.Ylabel = ""
        self.Title = ""
        
    def addLabel(self,label):
        self.labels.append(label)
    
    def xlabel(self,label):
        self.Xlabel = label

    def ylabel(self,label):
        self.Ylabel = label
    
    def title(self, title):
        self.Title = title

    def plot(self):
        handles = []
        index = np.array(range(0,50,5))
        index = index[1:]
        for i,d in enumerate(self.data):
            handles.append(plt.plot(index,d,'-o',label="data"+str(i)))

        plt.xlabel(self.Xlabel)
        plt.ylabel(self.Ylabel)
        plt.title(self.Title)
        plt.legend(self.labels)
        plt.show()

#%%
convE = methodData("metrics/convE.txt")
convE.readpath()
#%%
distmult = methodData("metrics/distmult.txt")
distmult.readpath()
#%%
hits5 = plotter()
hits10 = plotter()
mrr = plotter(convE.getMrr(), distmult.getMrr())
hits1 = plotter(convE.getHits1(), distmult.getHits1())
hits5 = plotter(convE.getHits5(), distmult.getHits5())
hits10 = plotter(convE.getHits10(), distmult.getHits10())
mrr.title("MRR plot per epochs")
mrr.addLabel("convE")
mrr.addLabel("distMult")
mrr.xlabel("messured epoch")
mrr.ylabel("MRR")
mrr.plot()

hits1.title("hits@1 plot per epochs")
hits1.addLabel("convE")
hits1.addLabel("distMult")
hits1.xlabel("messured epoch")
hits1.ylabel("hits@1")
hits1.plot()

hits5.title("hits@5 plot per epochs")
hits5.addLabel("convE")
hits5.addLabel("distMult")
hits5.xlabel("messured epoch")
hits5.ylabel("hits@5")
hits5.plot()

hits10.title("hits@10 plot per epochs")
hits10.addLabel("convE")
hits10.addLabel("distMult")
hits10.xlabel("messured epoch")
hits10.ylabel("hits@10")
hits10.plot()

# %%
