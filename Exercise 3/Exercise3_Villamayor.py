"""
GE 120
Erianne Villamayor
2023-11100

Machine Exercise 3
"""
#import necessary functions
from math import cos, sin, radians, sqrt, ceil

def getLatitude(distance, azimuth):

    """
    Compute for the Latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    Latitude - float
    """

    latitude = -distance * cos(radians(azimuth))

    return latitude

def getDeparture(distance, azimuth):
    """
    Compute for the departure of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    Departure - float
    """

    departure = -distance *sin(radians(azimuth))

    return departure

def azimuthToBearing(azimuth):
    """
    Compute for the DMS bearing of a given angle.

    Input:
    azimtuh - float

    Output:
    bearing - string
    """
#set up values for the angles
    if "-" in str(azimuth): #if the given is DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360

    else: 
        azimuth = float(azimuth)%360

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^15} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^15} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {: ^15} E'.format(azimuth - 180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^15} E'.format(360 - azimuth)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing == "DUE WEST"
    elif azimuth == 180:
        bearing == "DUE NORTH"
    elif azimuth == 270:
        bearing == "DUE EAST"
    else:
        bearing = "DNE"

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

#computing for the summations of bearing, lat, and dep
    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(azimuth=float(azimuth), distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth), distance=float(distance))

    sumLat += lat
    sumDep += dep
    sumDist += float(distance)

    line = (counter, distance, bearing, lat, dep) 
    lines.append(line)

#Setting up the Input and table
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "Yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print('{: ^20} {: ^20} {: ^20} {: ^20} {: ^20} {: ^20}'.format("LINE NO.", "DISTANCE", "AZIMUTH", "BEARING", "LATITUDE", "DEPARTURE"))

for line in lines:
    print('{: ^20} {: ^20} {: ^20} {: ^20} {: ^20} {: ^20}'.format(line[0], line[1], line[2], round(line[3], 2), round(line[4], 2), round(line[5-1], 2)))

print("SUMMATION OF LAT:", round(sumLat, 2))
print("SUMMATION OF DEP:", round(sumDep, 2))
print("SUMMATION OF DIST:", round(sumDist, 2))

lec = sqrt(sumLat**2 + sumDep**2)

print("LEC",lec)

rec = sumDist/lec

print("REC 1:  ", round(rec, -1))

#Get the corrected lat and dep and add it 
constCorrLat = -sumLat/sumDist
constCorrDep =  -sumDep/sumDist

for line in lines:
    corr_lat = constCorrLat*float(line[1])
    corr_dep = constCorrDep*float(line[1])

    adjLat = line[3] + corr_lat
    adjDep = line[4] + corr_dep


print("------END-------")

