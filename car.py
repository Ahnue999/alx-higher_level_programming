class Car:

    wheels = 4

car1 = Car()
print(car1.wheels)

Car.wheels = 2

car2 = Car()

print(car1.wheels)
print(car2.wheels)
