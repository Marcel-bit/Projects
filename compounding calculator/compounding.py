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
        for i in range(1, self.years):
            amount += self.recurring*((1+self.ann_percent)**(i))
        return amount
    
    '''def graph_part(self):
        maney = self.initial
        for i in range(1, self.years+1):
            
            maney = maney*((1+self.ann_percent)**(i))
            maney += self.recurring
            print(maney)'''
    

    
    #print out
    def string_part(self):
        i = self.initial_part()
        r = self.recurring_part()

        p = self.initial + (self.recurring*(self.years-1))

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
    