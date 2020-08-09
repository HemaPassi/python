import random
class Coin:
    def __init__(self, rare=False, clean = True, heads= True, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value) #it will loopthrough all the item in chicl and set like self.original_valu
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
    
    if self.is_clean:
        self.colour = self.clean_colour
    else :
        self.colour = self.rusty_colour
        
            
    def rust(self):   #first parameter of every class method should be self
        self.color = self.rusty_colour

    def clean(self):
        self.color = self.clean_colour

    def flip(self):
        head_options =[True, False]
        option = random.choice(head_options)
        self.heads=option      
            
    def __del__(self): # this is destructor  eg. del coin1 # coin1 is object of Pound 
        print('Coin spent')
        
class Pound(Coin):
    def __init__(self):
        data= {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_colour":"greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness":3.15,
            "mass":9.5
            }
        super().__init__(**data)  # it will destructuer dictionaary values in partent class
            
