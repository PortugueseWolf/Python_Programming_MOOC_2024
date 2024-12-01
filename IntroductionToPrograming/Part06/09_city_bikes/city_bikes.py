import math

def get_station_data(filename: str) -> dict:
    station_data = {}

    with open(filename) as file:
        for line in file:
            inf = line.split(";")
            if inf[0] == "Longitude":
                continue

            station_data[inf[3]] = (float(inf[0]),float(inf[1]))

    return station_data

def distance(stations: dict, station1: str, station2: str) -> float:

    if station1 == station2:
        return 0.0

    s1x = stations[station1][0]
    s2x = stations[station2][0]

    s1y = stations[station1][1]
    s2y = stations[station2][1]

    x_km = (s1x - s2x) * 55.26
    y_km = (s1y - s2y) * 111.2
    
    distance = math.sqrt(x_km**2 + y_km**2)

    return distance

def greatest_distance(stations: dict) -> tuple:
    greatest = 0.0
    first_name = ""
    second_name = ""

    i1 = 0
    i2 = 0

    for first in stations.items():
        for second in stations.items():
            if i2 <= i1:
                i2 += 1
                continue

            compare = distance(stations, first[0], second[0])

            if compare > greatest:
                greatest = compare
                first_name = first[0]
                second_name = second[0]
            
            i2 += 1
        
        i1 += 1
    
    return (first_name, second_name, greatest)

if __name__ == "__main__":
    a = distance(get_station_data("stations1.csv"),"Viiskulma", "Kaivopuisto")
    print(a)
    d = greatest_distance(get_station_data("stations1.csv"))
    print(d)
