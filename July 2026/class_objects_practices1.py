class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
    
        if type(name)  != str or type(planet_type)  !=  str or   type(star) != str:
            raise TypeError('name, planet type, and star must be strings')
        if not name or not planet_type or not star:
            raise ValueError('name, planet_type, and star must be non-empty strings')
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('earth', 'test', 'sun')
planet_2 = Planet('mars', 'test2', 'sun')
planet_3 = Planet('Jupiter', 'test3', 'sun')

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
print(planet_1)
print(planet_2)
print(planet_3)


#dunder methods

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
print(len(cart))        # 1
print('Laptop' in cart) # True


