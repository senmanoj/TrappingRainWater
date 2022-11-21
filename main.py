# Author : Manoj Sen
# Description : Trapping Rain Water where elevation map is given in form of array.
def trapwatercal(elevation_map, n):
    trapped_water = 0
    left_building = elevation_map[0]
    temp_water = 0
    for i in range(1, n):
        if elevation_map[i] >= left_building:
            trapped_water = trapped_water+temp_water
            temp_water = 0
            left_building = elevation_map[i]
        else:
            temp_water = temp_water + (left_building - elevation_map[i])
    return trapped_water

# DriverCode


eMap = [0, 1, 2, 0, 3, 8]
print(f"Trapped water unit is ", trapwatercal(eMap, len(eMap)))
