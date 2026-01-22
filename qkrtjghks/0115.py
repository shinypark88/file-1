##class Customer:
##    def __init__(self,name,customer_id):
##        self.name = name
##        self.customer_id = customer_id
##
##customer = Customer("박서환","060130")
##print(customer.name,customer.customer_id)
##customer.name = "이샘코딩학원"
##customer.customer_id = "123456"
##print(customer.name,customer.customer_id)

##class Customer:
##    def __init__(self,name,customer_id):
##        self.name = name
##        self.customer_id = customer_id
##    @property
##    def name(self):
##        return self.__name
##    def customer_id(self):
##        return self.__customer_id
##    @name.setter
##    def name(self,value):
##        self.__name = value
##    def customer_id(self,value):
##        self.__customer_id = value
##
##customer = Customer("박서환","060130")
##print(customer.name,customer.customer_id)
##customer.name = "이샘코딩학원"
##customer.customer_id = "123456"
##print(customer.name,customer.customer_id)

class Circle:
    PI=3.141592
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        return self.radius * self.radius * Circle.PI

class Cylinder(Circle):
    def __init__(self,area,height):
        super().__init__(area)
        super().get_area(height)
        self.height=height
        self.area = Circle.get_area
    def get_volume(self):
        return area * height

print(Cylinder(Circle(2.8),5.6))
