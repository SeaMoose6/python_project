import random
import math
'''
class Rocket():
    def __init__(self): #defult values second always
        self.height = 200
        self.x_loc = 0
        self.y_loc = 0
        self.rocket_velo = 10

    def move_up(self):
        self.y_loc -= self.rocket_velo



enemy_rockets = [Rocket() for i in range(1, 10)]


for rocket in enemy_rockets:
    print(rocket)
'''
# Q 1
'''
class Rocket():
    def __init__(self, x_loc=0, y_loc=0):
        self.x_loc = x_loc
        self.y_loc = y_loc
        
    def move_rocket(self, right_dis=0, up_dis=0):
        self.x_loc += right_dis
        self.y_loc += up_dis
        return self.x_loc, self.y_loc
        
    def get_distance(self, rocket):
        first_val = rocket.x_loc - self.x_loc
        first_val *= first_val
        second_val = rocket.y_loc - self.y_loc
        second_val *= second_val
        radical = first_val+second_val
        return math.sqrt(radical)


rocket1 = Rocket(0, 0)

"""print(rocket1.move_rocket(10, 40))
print(rocket1.move_rocket(45, 200))
print(rocket1.move_rocket(-510, 340))"""

rocket_fleet = [Rocket() for num in range(1, 10)]
rocket_fleet[1].move_rocket(50, 50)
rocket_fleet[7].move_rocket(20, 40)
rocket_fleet[0].move_rocket(500, 70)
rocket_fleet[4].move_rocket(150, 55)

#for rocket in rocket_fleet:
    #print(rocket.move_rocket(random.randint(1, 100), random.randint(1, 100)))
    #print(rocket.move_rocket())
print(rocket_fleet[1].get_distance(rocket_fleet[7]))
print(rocket_fleet[4].get_distance(rocket_fleet[7]))
print(rocket_fleet[0].get_distance(rocket_fleet[1]))
print(rocket_fleet[1].get_distance(rocket_fleet[4]))
'''

#Q 2
class Rocket():
    def __init__(self, rocket_speed, rocket_owner, rocket_price, x_loc=0, y_loc=0):
        self.rocket_speed = rocket_speed
        self.rocket_owner = rocket_owner
        self.rocket_price = rocket_price
        self.x_loc = x_loc
        self.y_loc = y_loc


rocket1 = Rocket(500, "Tony Stark", 1000000000, 50, 0)
print(rocket1.rocket_owner)
print(rocket1.rocket_speed)
print(rocket1.x_loc)
print(rocket1.rocket_price)

rocket_owners = ['Seamus Devon', 'Jeff', 'Elon Musk', 'Mark', 'Capitan America']
rocket_fleet = []

for num in range(0, 5):
    speed = 300*num
    price = 100000000+num*750000
    rocket_fleet.append(Rocket(speed, rocket_owners[num], price))

print(rocket_fleet)

print(rocket_fleet[4].rocket_owner)

#Q 3
'''
class Rocket():
    def __init__(self, rocket_speed, rocket_owner, rocket_price, x_loc=0, y_loc=0):
        self.rocket_speed = rocket_speed
        self.rocket_owner = rocket_owner
        self.rocket_price = rocket_price
        self.x_loc = x_loc
        self.y_loc = y_loc
        
    def move_rocket(self, right_dis=0, up_dis=0):
        self.x_loc += right_dis
        self.y_loc += up_dis
        return self.x_loc, self.y_loc

    def launch(self):
      print(f'{self.rocket_owner} is preparing for takeoff!')


    def land(self):
      print(self.x_loc, self.y_loc)
      self.x_loc = 0
      self.y_loc = 0
      print(self.x_loc, self.y_loc)
        
    def get_distance(self, rocket):
        first_val = rocket.x_loc - self.x_loc
        first_val *= first_val
        second_val = rocket.y_loc - self.y_loc
        second_val *= second_val
        radical = first_val+second_val
        return math.sqrt(radical)

    def safety_check(self, rocket):
      if 0 < self.get_distance(rocket) < 100:
        print('THE ROCKETS ARE TOO CLOSE!')
      elif self.get_distance(rocket) >= 100:
        print('The rockets are at a safe distance.')
      elif self.get_distance(rocket) == 0:
        print('THE ROCKETS HAVE CRASHED!!!')


rocket1= Rocket(500, "Tony Stark", 1000000000, 50, 0)
rocket1.launch()
rocket1.move_rocket(150, 45)
#rocket1.land()

print()

rocket2= Rocket(720, "Elon Msuk", 2500000000, 0, 40)
rocket2.launch()
rocket2.move_rocket(100, 5)
#rocket2.land()

print()

rocket1.safety_check(rocket2)
'''
#Q 4
class Person():
  def __init__(self, name, age, job, sibling_count):
    self.name = name
    self.age = age 
    self.job = job
    self.sibling_count = sibling_count

  def introduce_yourself(self):
    print(f'Hello, my name is {self.name} and I am {self.age} years old.')

  def job_status(self):
    print(f"I am currently employed at {self.job}")

  def growing(self):
    self.age += 1

person1 = Person('Sam', 24, 'Manager', 0)
person1.introduce_yourself()
person1.job_status()
print(person1.age)
person1.growing()
print(person1.age)

#Q 5
class Car():
  def __init__(self, color, seat_count, miles,      gas_tank, price):
    self.color = color
    self.seat_count = seat_count
    self.miles = miles
    self.gas_tank = gas_tank
    self.price = price
  
  def affordability(self):
    print(f'For the low low price of {self.price} dollars you can this car which is able to sit up to {self.seat_count} people and has {self.miles} miles on it!')
  
  def out_driving(self, miles):
    print(self.gas_tank, self.miles)
    self.gas_tank = 0
    self.miles -= miles
    print(self.gas_tank, self.miles)
    print('Gotta fuel up!')

car1 = Car('red', 2, 24000, 40, 75000)
car1.affordability()
car1.out_driving(5)
print()

car2 = Car('green', 5, 28000, 60, 40000)
car2.affordability()
car2.out_driving(15)
print()

car3 = Car('silver', 6, 32000, 50, 36000)
car3.affordability()
car3.out_driving(2)
print()

car4 = Car('black', 8, 80000, 80, 85000)
car4.affordability()
car4.out_driving(30)
print()
