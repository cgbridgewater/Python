from re import T


class Shoe:
    def __init__(self):
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


class Shoe():
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic SK8-Hi"
        self.price = 69.99
        self.in_stock = True


skater_shoe = Shoe()
dress_shoe = Shoe()

print(skater_shoe.type)
print(dress_shoe.type)

skater_shoe.type = "Low Top Trainers"
print(skater_shoe.type)

dress_shoe.type = "Ballet Slipper"
print(dress_shoe.type)



class Shoe:
    #our method has 4 parameters (including self)
    def __init__(self, brand, shoe_type, price):
        #we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        #the stock status is default set to True
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low Top Trainer", 59.99)
dress_shoe = Shoe("Jack and Jill Bootery", "Ballet Flats", 29.99)

print("-------new lines----------")
print(skater_shoe.type)
print(dress_shoe.type)

#add another shoe type and make the in stock status read False
golf_shoe = Shoe("Nike Golf", "Boa Golf Cleat", 129.99)
print(golf_shoe.type)
golf_shoe.in_stock = False
print(golf_shoe.in_stock)

