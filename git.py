class magazine():
    def __init__(self,cost,quantity,name):
        self.cost=cost
        self.quantity=quantity
        self.name=name
    def give_me_money(self):
        self.squa=self.cost*self.quantity
        print(self.squa,' грн вам нужно заплатить за товар под названием',self.name)

tria=magazine(5,5,'Bread')
tria.give_me_money()