import numpy as np

class FitnessFunctions:
    def __init__(self):
        self.ack_inital = [-32.768,32.768]
        self.ras_inital = [-5.12,5.12]
        self.sch_inital = [-500,500]
        self.ack_glob = 0
        self.ras_glob = 0
        self.sch_glob = 420.9687

        
    def ackely(self, x):
        n = np.size(x)
        n_inverse = 1/n
        sum1 = 0
        sum2 = 0
        for i in x:
            sum1 += i**2
            sum2 += np.cos(2*np.pi*i)
        return -20*(np.exp(-0.2*np.sqrt(n_inverse*sum1))) - np.exp(n_inverse*sum2) +20 + np.exp(1)

    def rastrigin(self,x):
        n = np.size(x)
        sum1 = 0
        for i in x:
            if i >= self.ras_inital[0] and i <= self.ras_inital[1]:
                sum1 += (i**2) - (10*np.cos(2*np.pi*i))
            else:
                sum1 += 10* (i**2)
        return 10*n + sum1

    def schwefel(self,x):
        n = np.size(x)
        sum1 = 0
        for i in x:
            if i >= self.ras_inital[0] and i <= self.ras_inital[1]:
                sum1 += -i *np.sin(np.sqrt(np.absolute(i)))
            else:
                sum1 += 0.02* (i**2)
        return 418.9829*n + sum1
# fun = FitnessFunctions()
# print(fun.ackely([-19.05801213,  10.29698605 ,-37.99031157 , 28.27758733  ,21.9383276,-64.66740954 , 73.41795275, -35.85573575, -29.23661105 , 89.60423853]))
# print(fun.ackely([-29.73705379 , -0.79466886 ,-35.37619616  ,19.99142907 , 21.81903689,-52.83460216 , 68.50780839, -29.5287941 , -23.06405103 , 92.85435103]))
# print(fun.ackely([-100.587,-35.62,-22,-40.139,13,-148.575,4.6307,110.1309,-4.00138,-47.87]))
