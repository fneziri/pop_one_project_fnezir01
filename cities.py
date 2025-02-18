
#for the visualise road map function (extension), matplotlib needs to be installed

import random
import math
import matplotlib.pyplot as plt


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
      [(state, city, latitude, longitude), ...] 
    Use this as your initial `road_map`, that is, the cycle 
      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    file = open(file_name, "r")
    road_map = []
    for line in file:
        road_map.append(tuple((line).strip().split("\t")))
    file.close()
    return road_map

  
def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    for element in road_map:
        print("City: " + str(element[1])\
              + " | Latitude: " + str(round(float(element[2]),2))\
              + " | Longitude: "+ str(round(float(element[3]),2)))
    
    
def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    total_distance = 0.0
    for i in range(0, len(road_map)):
        x1 = float(road_map[i][2])
        y1 = float(road_map[i][3])
        x2 = float(road_map[(i + 1) % len(road_map)][2])
        y2 = float(road_map[(i + 1) % len(road_map)][3])
        total_distance += math.dist((x1,y1),(x2,y2))
    return total_distance


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 
        (new_road_map, new_total_distance)
    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    new_road_map = road_map
    original_index = new_road_map[index1]
    if index1 != index2:
        new_road_map[index1] = new_road_map[index2]
        new_road_map[index2] = original_index
    else:
        pass
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    return road_map[-1:] + road_map[:-1]


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    new_road_map = road_map
    shortest_distance = compute_total_distance(road_map)
    best_cycle = []

    #swap_cities
    
    for i in range(0, 5000):
        index1 = int(len(road_map)*random.random())
        index2 = int(len(road_map)*random.random())
        swap_cities_output = swap_cities(new_road_map, index1, index2)
        new_road_map = swap_cities_output[0][:]
        distance_swap = float(swap_cities_output[1])
        if distance_swap < shortest_distance:
            shortest_distance = distance_swap
            best_cycle = new_road_map

    #shift_cities

    for i in range(0, 5000):
        new_road_map = shift_cities(new_road_map)
        distance_shift = compute_total_distance(new_road_map)
        if distance_shift < shortest_distance:
            shortest_distance = distance_shift
            best_cycle = new_road_map

    return best_cycle


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    for i in range(0, len(road_map)):
        x1 = float(road_map[i][2])
        y1 = float(road_map[i][3])
        x2 = float(road_map[(i + 1) % len(road_map)][2])
        y2 = float(road_map[(i + 1) % len(road_map)][3])
        cost_each_connection = math.dist((x1,y1),(x2,y2))
        print("Trip", i+1, "| Start point: " + road_map[i][1] + ", End point: "\
              + road_map[(i + 1) % len(road_map)][1] + " | Distance: ",\
              cost_each_connection)
    print("\nThe total distance is: ", compute_total_distance(road_map))
    

def visualise(road_map):
    longitudes = []
    latitudes = []
    
    for i in range(0,len(road_map)):
        longitudes.append(float(road_map[i][3]))
        latitudes.append(float(road_map[i][2]))
        
    plt.axis([-180,180,-90,90])
    plt.title("Road Map Visualised")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.plot(longitudes, latitudes, "ro")

    for i in range(0,len(road_map)):
        plt.annotate(i+1, xy = (longitudes[i], latitudes[i]))

    plt.show()
    

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    road_map = read_cities("city-data.txt")
    print("List of cities: \n")
    print_cities(road_map)
    best_road_map = find_best_cycle(road_map)
    print("\nThe optimal journey consists of the following trips: \n")
    print_map(best_road_map)
    visualise(best_road_map)


if __name__ == "__main__": #keep this in
    main()
