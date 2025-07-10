class hotel:
    hotel_name='shiv sagar'
    branch = 'matri mall'
    manager = 'Ram'
    items = {'dosa' :10,'pulav':4,'poori':6,'coffe':8}
    price= {'dosa' :100,'pulav':50,'poori':70,'coffe':20}
    def __init__(self,name,phno,table_no):
         self.name = name
         self.phno = phno
         self.table_no = table_no
         self.order ={}

    def display_order(self):
        print(self.order)
        
    def place_order(self,item,qty):
        if item in hotel.items:
            if qty<=hotel.items[item]:
                if item not in self.order:
                    self.order[item]=qty
                else:
                    self.order[item]+=qty
                hotel.items[item]-=qty
            else:
                print('order less quantity')
        else:
            print('item is not available')

    def cancel_order(self,item,qty):
        if item in self.order:
            if self.order[item] >=qty:
                self.order[item]-=qty
                hotel.items[item]+=qty
            else:
                print('can not cancel more times')
        else:
            print('item is not ordered')

    def gen_bill(self):
        amt=0
        for i in self.order:
            res=self.order[i]*hotel.price[i]
            amt+=res
            hotel.items[item]+=qty
        else:
            print('can not cancel more items')
    

    def geni_bill(self):
        amt=0
        for i in self.order:
            res=self.order[i]*hotel.price[i]
            amt+=res
        print(f'ur bill amount is {amt}')

c1=hotel('john',7026936758,4)
c1.place_order('dosa',5)
c1.place_order('coffe',2)
c1.geni_bill()
c1.display_order()
c1.cancel_order('coffe',1)
c1.geni_bill()
































        
