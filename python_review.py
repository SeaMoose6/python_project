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

class Rocket():
    def __init__(self, x_loc=0, y_loc=0):
        self.x_loc = x_loc
        self.y_loc = y_loc
    def mon_rocket(self, up_dis, down_dis, left_dis, right_dis):

