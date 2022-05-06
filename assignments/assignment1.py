#!/usr/bin/env python
 
import carla
from carla import VehicleLightState as vls
from numpy import random

client = carla.Client('127.0.0.1', 2000)  # specify the IP of the host and port
client.set_timeout(10.0)
print(client.get_client_version())
# print(client.get_available_maps())

world = client.load_world("circle_t_junctions")  # Loading the  world
map = world.get_map()
spawn_points = map.get_spawn_points()
spawn_point = spawn_points[0]  # Choosing 1 spawn point

blueprint_library = world.get_blueprint_library()
# print(blueprint_library)
walker = blueprint_library.filter('walker.*')
walker = walker[0]  # Choosing first walker 
pedestrain = world.spawn_actor(walker, spawn_point)

player_control = carla.WalkerControl()
player_control.speed = 3
pedestrain.apply_control(player_control)

spectator = world.get_spectator()  # Gets spectator from the world 
# Creating a new transformation to place the spectator
rotation = carla.Rotation()
new_location = carla.Location( x = -135, y =-30, z= 3)
new_transform = carla.Transform(new_location, rotation)
spectator.set_transform(new_transform)
# spectator.set_location(spawn_point)
# Notes Transform objects = Location and Transform 
