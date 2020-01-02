import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                 ("Delaware", "Dover", 39.161921, -75.526755),\
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)
 
    road_map2 = [("Wisconsin", "Madison", 43.074722, -89.384444),\
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042),\
                 ("Alabama", "Montgomery", 32.361538, -86.279118)]

    assert compute_total_distance(road_map2)==\
           pytest.approx(15.538+20.5+11.154, 0.01)

    road_map3 = [("Alaska", "Juneau", 58.301935, -134.41974),\
                 ("Hawaii", "Honolulu", 21.30895, -157.826182)]

    assert compute_total_distance(road_map3)==\
           pytest.approx(43.776*2, 0.01)

    road_map4 = [("Washington", "Olympia", 47.042418, -122.893077),\
                 ("West Virginia", "Charleston", 38.349497, -81.633294),\
                 ("Wisconsin", "Madison", 43.074722, -89.384444),\
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042)]

    assert compute_total_distance(road_map4)==\
           pytest.approx(42.166+9.078+15.538+19.028,0.01)

    road_map5 = [("New York", "Albany", 42.659829, -73.781339)]

    assert compute_total_distance(road_map5)==\
           pytest.approx(0.000,0.01) 
                 

def test_swap_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                 ("Delaware", "Dover", 39.161921, -75.526755),\
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    swap_road_map1 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                     ("Delaware", "Dover", 39.161921, -75.526755),\
                     ("Kentucky", "Frankfort", 38.197274, -84.86311)]

    road_map2 = [("Alaska", "Juneau", 58.301935, -134.41974),\
                 ("Hawaii", "Honolulu", 21.30895, -157.826182)]

    swap_road_map2 = [("Hawaii", "Honolulu", 21.30895, -157.826182),\
                      ("Alaska", "Juneau", 58.301935, -134.41974)]

    road_map3 = [("Washington", "Olympia", 47.042418, -122.893077),\
                 ("West Virginia", "Charleston", 38.349497, -81.633294),\
                 ("Wisconsin", "Madison", 43.074722, -89.384444),\
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042)]
    
    swap_road_map3 = [("Washington", "Olympia", 47.042418, -122.893077),\
                      ("Wisconsin", "Madison", 43.074722, -89.384444),\
                      ("West Virginia", "Charleston", 38.349497, -81.633294),\
                      ("Wyoming", "Cheyenne", 41.145548, -104.802042)]

    #for index 1 != index2
    
    assert swap_cities(road_map1,0,2) ==\
           (swap_road_map1, compute_total_distance(swap_road_map1))

    assert swap_cities(road_map2,0,1) ==\
           (swap_road_map2, compute_total_distance(swap_road_map2))

    assert swap_cities(road_map3,1,2) ==\
           (swap_road_map3, compute_total_distance(swap_road_map3))
    
    #for index1 = index2

    assert swap_cities(road_map1,1,1) ==\
           (road_map1, compute_total_distance(road_map1))

    assert swap_cities(road_map2,0,0) ==\
           (road_map2, compute_total_distance(road_map2))

    assert swap_cities(road_map3,3,3) ==\
           (road_map3, compute_total_distance(road_map3))

    
    

def test_shift_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                 ("Delaware", "Dover", 39.161921, -75.526755),\
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    shift_road_map1 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                       ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                       ("Delaware", "Dover", 39.161921, -75.526755)]

    assert shift_cities(road_map1) == shift_road_map1

    road_map2 = [("Wisconsin", "Madison", 43.074722, -89.384444),\
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042),\
                 ("Alabama", "Montgomery", 32.361538, -86.279118)]

    shift_road_map2 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                       ("Wisconsin", "Madison", 43.074722, -89.384444),\
                       ("Wyoming", "Cheyenne", 41.145548, -104.802042)]

    assert shift_cities(road_map2) == shift_road_map2

    road_map3 = [("Alaska", "Juneau", 58.301935, -134.41974),\
                 ("Hawaii", "Honolulu", 21.30895, -157.826182)]

    shift_road_map3 = [("Hawaii", "Honolulu", 21.30895, -157.826182),\
                       ("Alaska", "Juneau", 58.301935, -134.41974)]

    road_map4 = [("Washington", "Olympia", 47.042418, -122.893077),\
                 ("West Virginia", "Charleston", 38.349497, -81.633294),\
                 ("Wisconsin", "Madison", 43.074722, -89.384444),\
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042)]

    shift_road_map4 = [("Wyoming", "Cheyenne", 41.145548, -104.802042),\
                       ("Washington", "Olympia", 47.042418, -122.893077),\
                       ("West Virginia", "Charleston", 38.349497, -81.633294),\
                       ("Wisconsin", "Madison", 43.074722, -89.384444)]

    assert shift_cities(road_map4) == shift_road_map4

    road_map5 = [("New York", "Albany", 42.659829, -73.781339)]

    shift_road_map5 = [("New York", "Albany", 42.659829, -73.781339)]

    assert shift_cities(road_map5) == shift_road_map5


