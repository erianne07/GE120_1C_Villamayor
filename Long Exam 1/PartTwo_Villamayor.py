"""
GE 120
Erianne Villamayor

Direct Leveling Computations and finding 
the Geodetic Control Order given its vertical accuracy
"""

from cmd import PROMPT


def totalDistance(backsight, foresight):
    """
    Compute for the Distance between stations

    Input:
    backsight - float
    foresight - float

    Output:
    Distance - float
    """

    distance = (backsight * 100) + (foresight  * 100)

    return distance

#establish sentinel control loop and counter
tp_counter = 1
lines = []
sumDist = 0

#Creating prompt function
float(input(PROMPT))
Running_elevation = 100

#Define the what the True and False variables are
while True:
    print()
    print("TP", tp_counter)
   

    backsight = input("B.S ")
    foresight = input("F.S.: ")
    distance = (backsight * 100) + (foresight  * 100)



#Setting up the Input and table
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "Yes" or yn.lower() == "y":
        tp_counter = tp_counter + 1
        continue
    else:
        break

#Computing for Total Distance
BacksightDistance = backsight * 100
ForesightDistance = foresight * 100
height_of_the_instrument = Running_elevation - BacksightDistance
elevation_of_turning_point = BacksightDistance + height_of_the_instrument




levelling_table = (backsight, foresight, height_of_the_instrument, elevation_of_turning_point)
lines.append(levelling_table)

print("\n\n")
print('{: ^15} {: ^15} {: ^15} {: ^15} {: ^15}'.format("Sta.", "B.S", "H.I.", "F.S.", "Elev."))

for line in lines:
    print('{: ^15} {: ^15} {: ^15} {: ^15} {: ^15}'.format(line[0], line[1], line[2], line[3], line[4]))

print("------END------")