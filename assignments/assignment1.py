#!/usr/bin/env python

import carla
from carla import VehicleLightState as vls
from numpy import random

client = carla.Client('127.0.0.1', 2000)  # specify the IP of the host and port
client.set_timeout(10.0)
print(client.get_client_version())

world = client.get_world()  # default weorld is too large

world = client.load_world("cirle t_junctions")  # loading

spam_points = map.get_spam_points()

for point in spawn_points:
    print(point.location.x)

blueprint_library = world.get_blueprint_library()
vehicle = blue_print.giler('vehicle.audi.a2')
