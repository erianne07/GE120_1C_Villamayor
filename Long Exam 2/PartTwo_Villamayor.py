#import necessary functions
from math import cos, sin, radians, sqrt

class Parcel:
    owner = input("Name of Owner:")
    area = input("Area of Lot:")

    def __init__(self, area, classification):
        self.area = area
        self.classiication = classification

    def Classification(self):
        """
        get the classification of land based on the lot size.

        Input:
        area - float

        Output:
        classification - float
        """
        
        classification = -float(self.area) 
        
        return classification


    def area(self):
        """
        Compute for the area of a give lot.

        Input:
        lot - float

        Output:
        area - string
        """

#set up values for the area
    
        if area > 0 and area < 10000:
            classification = 'Residential'.format(round(area,3))
        elif area > 10000 and area < 120000:
            classification = 'Private Agricultural'.format(round(10000- area,3))
        elif area > 120000:
            classification = 'Public Agricultural'.format(round(area - 10000,3))
        else:
            classification = "DNE"

            return classification
#Print the function
print("A parcel of land owned by ")
        
class Riparian(Parcel):

    def __str__(self, area, classification):
        super().__init__(self, area, classification)
        
    def area(self):
        if area == 10000:
            classification = "Residential"
        elif area == 120000:
            classification = "Private Agricultural "
        else:
            classification = "EWAN KO"
        return classification
    
    def type(self):
        if type == 

#This is for the Sentinel Controlled Loop
counter = 1
lines = []

while True:
    print()
    print("CLASSIFICATION", )

    you_have_mistyped = False
    while not (you_have_mistyped):
        owner = input("Name of Owner:")
        area = input("Area: ")
        if you_have_mistyped:
            print("TRY AGAIN")
            continue
        if not(you_have_mistyped):
            break
    lot = input("Size of the Lot: ") 

   
    lines.append((counter, lines.distance, lines.area(), lines.lotType()))

#Setting up the Input and table
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "Yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format("DISTANCE", "AREA", "LAND CLASSIFICATION"))
for line in lines:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

print("------END-------")

