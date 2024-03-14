"""
GE 120
Erianne Villamayor
2023-11100

Machine Exercise 2
"""

#establish sentinel controlled loop and counter
counter = 1
lines = []

#Define the what the True and False variables are
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
    
    if "-" in azimuth: #in DMS
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


    line = (counter, distance, bearing) #created tuple of a line
    lines.append(line)


#Set up input
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "Yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break


print("\n\n")
print('{: ^15} {: ^15} {: ^15}'.format("LINE NO.", "DISTANCE", "AZIMUTH"))

for line in lines:
    print('{: ^15} {: ^15} {: ^15}'.format(line[0], line[1], line[2]))

print("------END------")

