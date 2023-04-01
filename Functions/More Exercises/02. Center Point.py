import math
distance_final = []
points = []

for i in range(2):
    x = float(input())
    y =  float(input())

    distance = math.sqrt((x - 0)**2 + (y - 0)**2)

    distance_final.append(distance)
    points.append(x)
    points.append(y)

if distance_final[0] <= distance_final[1]:
    print(f"({int(points[0])}, {int(points[1])})")
else:
    print(f"({int(points[2])}, {int(points[3])})")
    
## 80/100
