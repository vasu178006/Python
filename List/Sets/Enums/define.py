from enum import Enum
class Weekdays(Enum):
    sun=0
    mon=1
    tue=2
    wed=3
    thurs=4
    fri=5
    sat=6
print(Weekdays.sun)
print(Weekdays(1))
for day in Weekdays:
    print(day)
