class Shoe:
    def__init__(self):
        self.brand = "Adidas"
        self.type = "tennis shoes"
        self.price = 45.99
        self.in_stock = True

    def rebrand(self,new_brand): #rebrand updates brand of the shoe
        self.brand = new_brand

    def sold_out(self): #sold out changes in stock to be false
        self.in_stock = False

    def on_sale(self,percent): #on sale decreases the price by a certain percentage
        self.price = self.price * (1 - percent)

        


