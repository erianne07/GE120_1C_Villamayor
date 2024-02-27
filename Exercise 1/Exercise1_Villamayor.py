"""
GE 120: Intro
Erianne Villamayor
hi
"""

# dms = 118.42069

# #Kunin si degree part
# degree = int(dms)
# print("degree", 118)

# #Kunin si minutes
# minutes = (dms - degree) * 60

# minutes_fractional = int(minutes)

# seconds = (minutes - minutes_fractional) * 60

# print("minutes pero naka degree pa", minutes_fractional)
# print("seconds pero naka degree pa", seconds)

# print("DMS:" + str(degree) + "-" + str(minutes_fractional) + "-" + str(round(seconds, 2)))

#Must be a string input

dms = "118-25-14.48"
values= dms.split('-')


degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd = degrees + (minutes/60) + (seconds/3600)

print("ETO YUNG VALUE:", round(dd,6))
