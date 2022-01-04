import  numpy as np
from function import FitnessFunctions

class main:

    def __init__(self, function):
        # self.onefifth = 
        self.iteration = 0
        self.ps = 0
        self.sigma = 20
        self.function = function
        self.answer = True
        self.bestf = 0
        self.meanf = 0
        self.test = 0
        self.adaptiveES()
        
    def adaptiveES(self):
        self.p = self.initialPopulation(30,'ackely', 100)
        self.getfitness('ackely')
        print("best generation ",self.iteration, " : ", self.bestf)
        print("mean generation ",self.iteration, " : " , self.meanf)
        while self.iteration != 100 and self.answer:
            parents = self.uniform()
            # parents = self.tournament('ackley')
            offsprings = self.intermediatCrossover(parents, 0.6)
            self.onefifthmutation()
            self.getfitness('ackely')
            print("best generation ",self.iteration, " : ", self.bestf)
            print("mean generation ",self.iteration, " : " , self.meanf)


    def getfitness(self, funcname):
        if funcname == 'ackely': 
            fitness = self.function.ackely
        elif funcname == 'rastrigin': 
            fitness = self.function.rastrigin
        else:
            fitness = self.function.schwefel
        f = []
        for i in self.p:
            fitvalue = fitness(i)
            if fitvalue == 0:
                self.answer = False
            else:
                f.append(fitvalue)
        self.bestf = min(f)
        self.meanf = sum(f)/len(f)

    def onefifthmutation(self):
        sigma = self.sigma 
        c = 0.85 
        counter = 0
        
        for i in range(self.p.shape[0]):
            z = np.random.normal(0 ,sigma ,self.p.shape[1])
            oldfitness = self.function.ackely(self.p[i])
            self.p[i]= self.p[i]+ z
            newfitness = self.function.ackely(self.p[i])
            if oldfitness > newfitness :
                counter += 1
        self.ps = ((self.iteration*self.p.shape[0]* self.ps) + counter)/((self.iteration+1)*self.p.shape[0])
        print(self.ps , counter)
        self.iteration += 1
        if self.ps > 1/5: sigma = sigma/c
        elif self.ps < 1/5: sigma = sigma*c
        else: pass
        self.sigma = sigma

    def uniform(self):
        p = np.concatenate((self.p,self.p), axis=0)
        np.random.shuffle(p)
        p = p[np.random.choice(p.shape[0],int(p.shape[0]/2))]
        # print(p)
        return p

    def intermediatCrossover(self,p, alpha):
        mu = np.shape(p)[0]
        n = np.shape(p)[1]
        p = np.concatenate((p,p), axis=0)
        np.random.shuffle(p)
        z = np.zeros((mu,n)) #matrix for offsprings
        p1 = p[0:mu]
        p2 = p[mu:]
        for i in range(mu):
            for j in range(n):
                z[i][j]=(alpha*p1[i][j]) + (1-alpha)*p2[i][j]
        return z

    def tournament (self, funcname):
        if funcname == 'ackely': 
            fitness = self.function.ackely
        elif funcname == 'rastrigin': 
            fitness = self.function.rastrigin
        else:
            fitness = self.function.schwefel

        p = np.concatenate((self.p,self.p), axis=0)
        np.random.shuffle(p)
        mu = np.shape(self.p)[0]
        z = []
        for i in range(mu):
            tindex = np.random.choice(p.shape[0],3)
            t = np.array([p[j] for j in tindex])
            f = [fitness(j) for j in t]
            # print(f)
            maximum = f.index(max(f))
            z.append(t[maximum])
            p = np.delete(p,tindex[maximum], axis=0)
        return np.array(z)

    def initialPopulation (self, n,func, mu):
        p = np.zeros((mu,n))
        if func == 'ackely': 
            inital = self.function.ack_inital
        elif func == 'rastrigin': 
            inital = self.function.ras_inital
        else:
            inital = self.function.sch_inital

        for i in range(0,mu):
            for j in range(0,n):
                #func is the intial value of our function specified in its class
                p[i][j] = np.random.uniform(inital[0],inital[1])
        return p

function = FitnessFunctions()
main = main(function)