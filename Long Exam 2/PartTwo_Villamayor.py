#import necessary functions
from math import cos, sin, radians, sqrt

class Parcel:

    def __init__(self, area, distance, lot):
        self.area = area
        self.distance = distance
        self.lot = lot

    def lot(self):
        """
        Compute for the lot of given parcel of land.

        Input:
        distance - float

        Output:
        lot - float
        """
        
        lot = -float(self.distance) * cos(radians(self.azimuth))
        
        return 

    def distance(self):
        """
        Compute for the departure of a given line.

        Input:
        distance - float
        azimuth - float

        Output:
        Departure - float
        """

        departure = -float(self.distance) * sin(radians(self.azimuth))

        return departure

    def area(self):
        """
        Compute for the area of a give lot.

        Input:
        lot - float

        Output:
        area - string
        """

#set up values for the angles
    
        if lot > 0 and lot < 10000:
            area = 'Residential'.format(round(area,3))
        elif lot > 10000 and lot < 120000:
            area = 'Private Agricultural'.format(round(10000- area,3))
        elif lot > 120000:
            area = 'Public Agricultural'.format(round(area - 10000,3))
        else:
            area = "DNE"

            return area
        
class Cardinal(Parcel):

    def __init__(self, distance, azimuth):
        super().__init__(distance, azimuth)
        
    def area(self):
        if lot == 0:
            area = "DUE SOUTH"
        elif azimuth == 90:
            bearing = "DUE WEST"
        elif azimuth == 180:
            bearing = "DUE NORTH"
        elif azimuth == 270:
            bearing = "DUE EAST"
        else:
            bearing = "EWAN KO"
        return bearing

#This is for the Sentinel Controlled Loop
counter = 1
lines = []

while True:
    print()
    print("LINE NO.", counter)

    you_have_mistyped = False
    while not (you_have_mistyped):
        distance = input("Distance: ")
        if you_have_mistyped:
            print("TRY AGAIN")
            continue
        if not(you_have_mistyped):
            break
    lot = input("Size of the Lot: ") 

    if "-" in str(azimuth): #if the given is DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else: 
        azimuth = float(azimuth)%360

    if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    else:
        line = Parcel(distance, azimuth)


   
    lines.append((counter, line.distance, line.bearing(), line.latitude(), line.departure()))

#Setting up the Input and table
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "Yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format())
for line in lines:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2], round(line[3],3), round(line[4],3)))

print("------END-------")

