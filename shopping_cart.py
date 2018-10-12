class ShoppingCart:
    
    def __init__(self, employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount
        self._count = 0
        self._price_list = []
        
    def get_items(self):
        return self._items
    
    def get_total(self):
        return self._total
    
    def get_discount(self):
        return self._employee_discount
    
    total = property(get_total)
    items = property(get_items)
    employee_discount = property(get_discount)
        
    
    def add_item(self, name, price, quantity=1):
        if name not in self._items:
            self._items.append({'item': name, 'price': float(price), 'quantity': quantity})
        self._total += price * quantity
        self._count += quantity
        self._price_list = [price] * quantity
        return self._total
    
    def mean_item_price(self):
        return round(self._total/self._count, 2)
    
    def median_item_price(self):
        idx = len(self._price_list) // 2
        if len(self._price_list) % 2 == 0:
            return (self._price_list[idx] + self._price_list[idx -1])/2
        else:
            return self._price_list[idx]
    
    def apply_discount(self):
        if self._employee_discount != None:
            discount = (100 - self._employee_discount)/100
            return round(discount * self._total, 2)
        else:
            return "Sorry, there is no discount to apply to your cart :("
         
    def item_names(self):
        self._list_names = []
        for i in self._items:
            if i['quantity'] > 1:
                for q in range(i['quantity']):
                    self._list_names.append(i['item'])             
            else:
                self._list_names.append(i['item'])
        return self._list_names
        
    def void_last_item(self):
        if len(self._price_list) > 0:
            self._total -= self._price_list[-1]
        else:
            return "There are no items in your cart!"
