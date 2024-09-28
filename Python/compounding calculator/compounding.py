import matplotlib
import matplotlib.pyplot as plt

class Compounding:
    def __init__(self, initial, recurring, years, ann_percent):
        self.initial = initial
        self.recurring = recurring
        self.years = years
        self.ann_percent = ann_percent
    
    #calculate the final investment of the initial purchase
    def initial_part(self):
        return self.initial*((1+self.ann_percent)**self.years)
    
    #calculate final investment of recurring purchases
    def recurring_part(self):
        amount = 0
        for i in range(self.years):
            amount += (self.recurring*((1+self.ann_percent)**(i))) 
        return amount
    
    #graph for initial amount
    def graph_initial(self):
        lst = [0]
        for i in range(self.years):
            lst.append(self.recurring*((1+self.ann_percent)**(i))) 
        print()
        a = [self.initial*((1+self.ann_percent)**x) for x in range(self.years + 1)]
        total = []
        for x in range(self.years+1):
            curr = 0
            curre = []
            for y in range(x+1):
                if x > 0:
                    curre.append(lst[y])
                else:
                    curr += lst[x]
                    break
            curr += sum(curre)
                
            curr += a[x]
            total.append(curr)

        ypoints = total
        xpoints = [x for x in range(self.years+1)]
        print(ypoints, xpoints)
        print(f'Final amount : {total[-1]:.2f}')

        plt.plot(xpoints, ypoints)
        plt.show()
    
    #print out
    def string_part(self):
        i = self.initial_part()
        r = self.recurring_part()

        p = self.initial + (self.recurring*(self.years))

        print("-"*32)
        print()

        print(f"initial investment    : {round(self.initial, 2)}$")
        print(f"reccuring investment  : {round(self.recurring, 2)}$")
        print(f"years of compounding  : {self.years}")
        print(f"annual percentage     : {round(self.ann_percent*100, 2)}%")
        print()

        print(f"total principal       : {round(p, 2)}$")
        print(f"final result          : {round(i + r, 2)}$")
        print(f"Return On Investment  : {round((((i + r)-p)/p)*100, 2)}%")

        print()
        print("-"*32)


        return i + r
    