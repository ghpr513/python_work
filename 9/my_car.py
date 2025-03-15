import car

my_new_car = car.Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_mustang = car.Car('ford', 'musting', 2024)
print(my_mustang.get_descriptive_name())
my_leaf =  car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())