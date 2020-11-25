# transmissionLoss.py
#
# Rahul Kalampattel
# Created: 24/11/2020
# Updated: 24/11/2020

import arlpy.uwapm as uwapm
import arlpy.uwa as uwa
import numpy as np

bathy = [
    [0, 30],    # 30 m water depth at the transmitter
    [300, 20],  # 20 m water depth 300 m away
    [1000, 25]  # 25 m water depth at 1 km
]

ssp = [
    [0, 1540],  # 1540 m/s at the surface
    [10, 1530],  # 1530 m/s at 10 m depth
    [20, 1532],  # 1532 m/s at 20 m depth
    [25, 1533],  # 1533 m/s at 25 m depth
    [30, 1535]   # 1535 m/s at the seabed
]

env = uwapm.create_env2d(
    depth=bathy,
    soundspeed=ssp,
    bottom_soundspeed=1450,
    bottom_density=1200,
    bottom_absorption=1.0,
    tx_depth=15
)

# uwapm.print_env(env)

# uwapm.plot_env(env, width=900)

# uwapm.plot_ssp(env)

# rays = uwapm.compute_eigenrays(env)
# uwapm.plot_rays(rays, env=env, width=900)

# arrivals = uwapm.compute_arrivals(env)
# uwapm.plot_arrivals(arrivals, width=900)
# print(arrivals[arrivals.arrival_number < 10]
#       [['time_of_arrival', 'angle_of_arrival',
#         'surface_bounces', 'bottom_bounces']])

env['rx_range'] = np.linspace(0, 1000, 1001)
env['rx_depth'] = np.linspace(0, 30, 301)

beampattern = np.array([
    [-180,  10], [-170, -10], [-160,   0], [-150, -20], [-140, -10], [-130, -30],
    [-120, -20], [-110, -40], [-100, -30], [-90 , -50], [-80 , -30], [-70 , -40],
    [-60 , -20], [-50 , -30], [-40 , -10], [-30 , -20], [-20 ,   0], [-10 , -10],
    [  0 ,  10], [ 10 , -10], [ 20 ,   0], [ 30 , -20], [ 40 , -10], [ 50 , -30],
    [ 60 , -20], [ 70 , -40], [ 80 , -30], [ 90 , -50], [100 , -30], [110 , -40],
    [120 , -20], [130 , -30], [140 , -10], [150 , -20], [160 ,   0], [170 , -10],
    [180 ,  10]
])
env['tx_directionality'] = beampattern

surface = np.array([[r, 0.5+0.5*np.sin(2*np.pi*0.005*r)] for r in np.linspace(0, 1000, 1001)])
env['surface'] = surface

tloss = uwapm.compute_transmission_loss(env, mode='incoherent')
# uwapm.plot_transmission_loss(tloss, env=env, clim=[-60,-30], width=900)

tloss.to_csv('transmissionLossRaw.csv')


def calculate_ss(t, d):
    ss = uwa.soundspeed(temperature=t, depth=d)
    return ss
