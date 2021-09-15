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