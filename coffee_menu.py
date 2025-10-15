class CoffeeMenu:
    
    def __init__(self):
        self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

    def get_price_existing_item(self, item):
        #if item in self.menu:
        return self.menu.get(item.lower())
        #raise ValueError('Item does not exist.')
    
    def add_item(self, item, price):
        self.menu[item.lower()] = price
        
            
    