# environment.py
#
# Input file, defines environmental properties
#
# Rahul Kalampattel
# Created: 26/11/2020
# Updated: 26/11/2020

import pandas as pd
import numpy as np

# Depth dependent sound speed as an array
ssp = [
    [0, 1540],  # 1540 m/s at the surface
    [10, 1530],  # 1530 m/s at 10 m depth
    [20, 1532],  # 1532 m/s at 20 m depth
    [25, 1533],  # 1533 m/s at 25 m depth
    [30, 1535]   # 1535 m/s at the seabed
]

# Range and depth dependent sound speed as a data frame
# ssp = pd.DataFrame({
#           0: [1540, 1530, 1532, 1533],     # profile at 0 m range
#         100: [1540, 1535, 1530, 1533],     # profile at 100 m range
#         200: [1530, 1520, 1522, 1525] },   # profile at 200 m range
#         index=[0, 10, 20, 30])             # depths of the profile entries in m

# Bottom depth profile
# depth = [
#     [0, 30],    # 30 m water depth at the transmitter
#     [300, 20],  # 20 m water depth 300 m away
#     [1000, 25]  # 25 m water depth at 1 km
# ]

max_depth = 30

# Bottom properties
bottom_absorption = 1.0
bottom_density = 1200
bottom_soundspeed = 1450

# Surface profile
surface = np.array([[r, 0.5+0.5*np.sin(2*np.pi*0.005*r)] for r in np.linspace(0, 1000, 1001)])
