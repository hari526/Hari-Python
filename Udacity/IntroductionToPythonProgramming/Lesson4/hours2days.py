"""
This is regualar method 
def hours2days(hours):
     days=hours//24
     hour=hours%24
     print("{} Days and {} Hours".format(days,hour))

hours2days(26)
"""

""" trying with the tuples"""
def hours2days(hours):
    days=hours//24
    hour=hours%24
    return (days,hour)

test=hours2days(19)
print("Tuple for hours2days",test)
