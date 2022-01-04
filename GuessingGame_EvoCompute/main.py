import random
import numpy as np

class guessMySentence:
    def __init__(self, name = None):
        self.geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"
        self.target = "Hanieh"
        self.population = 100
        self.parent = initial_pop(self.target, self.population, self.geneset) #creates intial population for algorithm
        self.pm = 1
        self.success = 0
        self.count = 0
        self.flag = False
        self.iteration = 0

    def genetic(self):
        while (self.flag == False and self.iteration < 1000 ):
            winner = []
            for i in range(0,self.population*2) :
                winner.append(self.tournamant())
            offspring = self.recombination(winner)
            offspring = self.mutation(offspring)
            # self.parameter()
            self.parent = self.survival(offspring)

    def survival(self, offspring):
        pop = self.parent + offspring
        generation = [[0 for x in range(2)] for y in range(len(pop))]
        for i in range(len(pop)):
            generation[i][0] = pop[i]
            generation[i][1] = self.get_fitness(pop[i], self.target)
        generation.sort(key = lambda x:x[1], reverse =True)
        for i in range(self.population):
            self.parent[i] = generation[i][0]
        print(generation[0], self.iteration)
        self.iteration = self.iteration + 1
        return self.parent

    def tournamant(self):
        result = []
        opponent = random.sample(self.parent, 2)
        for i in opponent:
            result.append(self.get_fitness(i, self.target))
        if result[0] == result[1]: 
            a = random.sample(opponent,1)
            return a[0]
        return opponent[result.index(max(result))]

    def recombination(self,winner):
        offspring = []
        for i in range(0,self.population):
            p1 = winner[i] 
            p2 = winner[self.population+i]
            offspring.append(self.crossover(p1,p2))
        return offspring
        
    def crossover(self, p1, p2):
        # cpoint = random.sample(list(range(len(p1))), 2) #generating 2 unique random points for cross over.
        # cpoint.sort()
        # child = random.sample([p1[0:cpoint[0]],p2[0:cpoint[0]]],1)[0] + random.sample([p1[cpoint[0]:cpoint[1]],p2[cpoint[0]:cpoint[1]]],1)[0] + random.sample([p1[cpoint[1]:],p2[cpoint[1]:]],1)[0]
        point = random.randint(0,len(p1)-1)
        child = random.sample([p1[0:point],p2[0:point]],1)[0] + random.sample([p1[point:],p2[point:]],1)[0]

        return child

    def get_fitness(self, guess, target):
        fitness = sum(1 for expected, actual in zip(target, guess)
            if expected == actual)
        if fitness == len(target): self.flag = True
        return fitness

    def mutation(self, offspring):
        for chrom in offspring:
            change = 0
            holder = chrom
            lchrom = list(chrom)

            for i in range(len(chrom)):
                check = random.randrange(0,100)/100
                if check < self.pm :
                    gen = random.sample(self.geneset ,1)[0]
                    lchrom[i] = gen
                    change = 1
            if change == 1 :
                chrom = ''.join(lchrom)
                self.count = self.count + 1
                old = self.get_fitness(holder, self.target)
                new = self.get_fitness(chrom , self.target)
                if new > old :
                    self.success = self.success + 1
        return offspring

    def parameter(self):
        ps = self.success / self.count
        if ps > 0.2:
            self.pm = self.pm / 0.8
        elif ps < 0.2:
            self.pm = self.pm * 0.8
        else:
            pass
    
def initial_pop(target, population, geneset):
    parent = []
    for i in range(0,population):
        genes = random.sample(geneset, len(target))
        genes = ''.join(genes)
        parent.append(genes)
    return parent

if __name__ == '__main__':
    run = guessMySentence()
    run.genetic()
