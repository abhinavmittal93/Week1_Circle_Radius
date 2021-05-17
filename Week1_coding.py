import math
import datetime

def calc_radius():
    radius = float(input('Enter the radius of the circle: '))
    area = math.pi * radius**2
    print(f'Area of the circle is: {area:.2f}')


def print_date_time():
    time = datetime.datetime.now()
    print(f'Today\'s date: {time}')


print_date_time()
calc_radius()

