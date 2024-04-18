"""
GE 120
Erianne Villamayor
2023-11100

Machine Exercise 4
"""
#import necessary functions
from math import cos, sin, radians, sqrt

class Line:

    def __init__(self, distance, azimuth):
        self.distance = distance
        self.azimuth = azimuth

    def latitude(self):
        """
        Compute for the Latitude of a given line.

        Input:
        distance - float
        azimuth - float

        Output:
        Latitude - float
         """
        
        latitude = -float(self.distance) * cos(radians(self.azimuth))
        
        return latitude

    def departure(self):
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

    def bearing(self):
        """
        Compute for the DMS bearing of a given angle.

        Input:
        azimuth - float

        Output:
        bearing - string
        """

#set up values for the angles
    
        if azimuth > 0 and azimuth < 90:
            bearing = 'S {: ^5} W'.format(round(azimuth,3))
        elif azimuth > 90 and azimuth < 180:
            bearing = 'N {: ^5} W'.format(round(180 - azimuth,3))
        elif azimuth > 180 and azimuth < 270:
            bearing = 'N {: ^5} E'.format(round(azimuth - 180,3))
        elif azimuth > 270 and azimuth < 360:
            bearing = 'S {: ^5} E'.format(round(360 - azimuth,3))
        else:
            bearing = "DNE"

            return bearing
        
class Cardinal(Line):

    def __init__(self, distance, azimuth):
        super().__init__(distance, azimuth)
        
    def bearing(self):
        if azimuth == 0:
            bearing = "DUE SOUTH"
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
sumLat = 0
sumDep = 0
sumDist = 0

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
    azimuth = input("Azimuth from the South: ") 

    if "-" in str(azimuth): #if the given is DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else: 
        azimuth = float(azimuth)%360

    if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    else:
        line = Line(distance, azimuth)

    sumLat += line.latitude()
    sumDep += line.departure()
    sumDist += float(line.distance)
   
    lines.append((counter, line.distance, line.bearing(), line.latitude(), line.departure()))

#Setting up the Input and table
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "Yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format("LINE NO. ", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in lines:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2], round(line[3],3), round(line[4],3)))

print("SUMMATION OF LAT:", round(sumLat, 2))
print("SUMMATION OF DEP:", round(sumDep, 2))
print("SUMMATION OF DIST:", round(sumDist, 2))

lec = sqrt(sumLat**2 + sumDep**2)

print("LEC",lec)
rec = sumDist/lec
print("REC 1:  ", round(rec, -3))

#Get the corrected lat and dep and add it 
constCorrLat = -sumLat/sumDist
constCorrDep =  -sumDep/sumDist

for line in lines:
    corr_lat = constCorrLat*float(line[1])
    corr_dep = constCorrDep*float(line[1])

    adjLat = line[3] + corr_lat
    adjDep = line[4] + corr_dep


print("------END-------")

