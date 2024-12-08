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

    #print out
    def string_part(self):
        i = self.initial_part()
        r = self.recurring_part()

        p = self.initial + (self.recurring*(self.years))

        results = {"principal": p, "final" : i + r, "roi" : (((i + r)-p)/p)*100}


        return results