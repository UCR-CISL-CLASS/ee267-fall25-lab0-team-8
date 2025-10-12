import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()

# Set up the simulator in synchronous mode
settings = world.get_settings()
settings.synchronous_mode = True # Enables synchronous mode
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings)

# Set up the TM in synchronous mode
traffic_manager = client.get_trafficmanager()
traffic_manager.set_synchronous_mode(True)

# Set a seed so behaviour can be repeated if necessary
traffic_manager.set_random_device_seed(0)
random.seed(0)

# We will aslo set up the spectator so we can see what we do
spectator = world.get_spectator()

spawn_points = world.get_map().get_spawn_points()

# Select some models from the blueprint library
models = ['dodge', 'audi', 'model3', 'mini', 'mustang', 'lincoln', 'prius', 'nissan', 'crown', 'impala']
blueprints = []
for vehicle in world.get_blueprint_library().filter('*vehicle*'):
    if any(model in vehicle.id for model in models):
        blueprints.append(vehicle)

# Set a max number of vehicles and prepare a list for those we spawn
max_vehicles = 50
max_vehicles = min([max_vehicles, len(spawn_points)])
vehicles = []

# Take a random sample of the spawn points and spawn some vehicles
for i, spawn_point in enumerate(random.sample(spawn_points, max_vehicles)):
    temp = world.try_spawn_actor(random.choice(blueprints), spawn_point)
    if temp is not None:
        vehicles.append(temp)

# Parse the list of spawned vehicles and give control to the TM through set_autopilot()
for vehicle in vehicles:
    vehicle.set_autopilot(True)
    # Randomly set the probability that a vehicle will ignore traffic lights
    traffic_manager.ignore_lights_percentage(vehicle, random.randint(0,50))

#Get Valid Spawn Points
p_spawn_points = []
for _ in range(200):  
    loc = world.get_random_location_from_navigation()
    if loc:  
        p_spawn_points.append(carla.Transform(loc))

# Get Pedestrian Blueprint
pedestrian_bp = random.choice(world.get_blueprint_library().filter('*walker.pedestrian*'))

# Limit number of pedestrians based on valid spawn points
max_pedestrians = 200
max_pedestrians = min(max_pedestrians, len(p_spawn_points))
pedestrians = []

#Take a random sample of spawn points and spawn pedestrians
for i, spawn_point in enumerate(random.sample(p_spawn_points, max_pedestrians)):
    actor = world.try_spawn_actor(pedestrian_bp, spawn_point)
    if actor:
        pedestrians.append(actor)

while True:
    world.tick()
