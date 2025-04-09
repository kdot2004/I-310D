#Import math to get the exact value of pi
import math

#The volume of a sphere is 4/3 * pi * (radius)^3
#Meaning four thirds multplied by pi the multiplied by the radius to the third power
#For this I'll define a function
def volume_of_sphere(radius):
    volume = 4/3 * math.pi * (radius)**3
    return volume

volume_30 = volume_of_sphere(30)
volume_40 = volume_of_sphere(40)
print(f'The volume of a sphere with a radius of 30 is {volume_30:,.2f}')
print(f'The volume of a sphere with a radius of 40 is {volume_40:,.2f}')