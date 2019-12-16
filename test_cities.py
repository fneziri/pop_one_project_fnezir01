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

def test_swap_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    total_distance1 = compute_total_distance(road_map1)
    
    new_road_map1 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                    ("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311)]
    
    new_total_distance1 = compute_total_distance(new_road_map1)

    #for index 1 != index2
    
    assert swap_cities(road_map1,0,2) ==\
           (new_road_map1, new_total_distance1)

    #for index1 = index2

    assert swap_cities(road_map1,1,1) ==\
            (road_map1, total_distance1)                     

def test_shift_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    new_road_map1 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                     ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                     ("Delaware", "Dover", 39.161921, -75.526755)]

    assert shift_cities(road_map1) == new_road_map1

    road_map2 = [("Washington", "Olympia", 47.042418, -122.893077),\
                  ("West Virginia", "Charleston", 38.349497, -81.633294),\
                  ("Wisconsin", "Madison", 43.074722, -89.384444),\
                  ("Wyoming", "Cheyenne", 41.145548, -104.802042)]

    new_road_map2 = [("Wyoming", "Cheyenne", 41.145548, -104.802042),\
                      ("Washington", "Olympia", 47.042418, -122.893077),\
                      ("West Virginia", "Charleston", 38.349497, -81.633294),\
                      ("Wisconsin", "Madison", 43.074722, -89.384444)]

    assert shift_cities(road_map2) == new_road_map2


    


