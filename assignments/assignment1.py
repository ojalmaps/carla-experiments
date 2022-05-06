#!/usr/bin/env python

import carla
from carla import VehicleLightState as vls
from numpy import random

client = carla.Client('127.0.0.1', 2000)  # specify the IP of the host and port
client.set_timeout(10.0)
print(client.get_client_version())

# print(client.get_available_maps())
world = client.load_world("circle_t_junctions")  # loading
map = world.get_map()
spawn_points = map.get_spawn_points()
spawn_point = spawn_points[0]  # Choosing 1 spawn point

blueprint_library = world.get_blueprint_library()
# print(blueprint_library)
walker = blueprint_library.filter('walker.*')
walker = walker[0]
print(walker)

pedestrain = world.spawn_actor(walker, spawn_point)

blueprint = world.get_blueprint_library().find('sensor.camera.rgb')
walker_controller_bp = world.get_blueprint_library().find('controller.ai.walker')

# Modify the attributes of the blueprint to set image resolution and field of view.
# blueprint.set_attribute('image_size_x', '1920')
# blueprint.set_attribute('image_size_y', '1080')
# blueprint.set_attribute('fov', '110')
# # Set the time in seconds between sensor captures
# blueprint.set_attribute('sensor_tick', '1.0')