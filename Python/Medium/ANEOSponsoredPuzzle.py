  
import sys
import math

max_speed = int(input())
light_count = int(input())
print("max_speed, light_count = ({}, {})".format(
    max_speed, light_count), file=sys.stderr)
tmp_speeds = [speed for speed in range(1, max_speed + 1)]

for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    print("Light {} : distance, duration = ({}, {})".format(
          i, distance, duration), file=sys.stderr)

    for speed in list(tmp_speeds):
        speedSec = (speed * 1000) / 3600
        timeToLight = distance / speedSec
        if math.floor(round(timeToLight / duration, 10)) % 2 == 1:
            tmp_speeds.pop(tmp_speeds.index(speed))

print("tmp_speeds = {}".format(tmp_speeds), file=sys.stderr)

print(max(tmp_speeds))