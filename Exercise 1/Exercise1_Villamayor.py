"""
GE 120
Erianne Villamayor
Machine Exercise 1
"""

dms = 118.42069

#Get the Degrees
degree = int(dms)
print("degree", 118)

#Get the Minutes
minutes = (dms - degree) * 60

minutes_fractional = int(minutes)

#Get Seconds
seconds = (minutes - minutes_fractional) * 60

print("minutes:", minutes_fractional)
print("seconds:", seconds)


#Combine to make DMS
print("DMS:" + str(degree) + "-" + str(minutes_fractional) + "-" + str(round(seconds, 2)))


# Must be a string input

dms = "118-25-14.48"
values= dms.split('-')


degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])


dd = degrees + (minutes/60) + (seconds/3600)

print("Value of DD:", round(dd,6))
