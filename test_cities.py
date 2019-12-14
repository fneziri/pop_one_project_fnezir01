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
    assert swap_cities == 'city1'
    

def test_shift_cities():
    '''add your tests'''
    assert shift_cities == 'the new road map'


