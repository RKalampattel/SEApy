# environment.py
#
# Input file, defines environmental properties
#
# Rahul Kalampattel
# Created: 26/11/2020
# Updated: 27/11/2020

import pandas as pd
import numpy as np

import scenario

# =============================================================================
# Sound speed profile
# =============================================================================
# ssp = 1500

# Depth dependent sound speed as an array
ssp = [
    [0, 1540.4],   # Speed at the surface
    [10, 1540.5],
    [20, 1540.7],
    [30, 1534.4],
    [50, 1523.3],
    [75, 1519.6],
    [100, 1518.5]  # Speed at the seabed
]

# Range and depth dependent sound speed as a data frame
# ssp = pd.DataFrame({
#           0: [1540, 1530, 1532, 1533],     # profile at 0 m range
#         100: [1540, 1535, 1530, 1533],     # profile at 100 m range
#         200: [1530, 1520, 1522, 1525] },   # profile at 200 m range
#         index=[0, 10, 20, 30])             # depths of the profile entries in m

# =============================================================================
# Bottom parameters
# =============================================================================
depth = 100

# Varying bottom depth profile
# depth = [
#     [0, 30],    # 30 m water depth at the transmitter
#     [300, 20],  # 20 m water depth 300 m away
#     [1000, 25]  # 25 m water depth at 1 km
# ]

# Bottom properties
bottom_absorption = 1.0
bottom_density = 1200

# =============================================================================
# Surface parameters
# =============================================================================
surface = None

# Surface profile
# surface = np.array([[r, 0.5+0.5*np.sin(2*np.pi*0.005*r)]
#                     for r in np.linspace(0, scenario.rx_range, 1+scenario.rx_range)])


# =============================================================================
# Ambient noise
# =============================================================================
sea_state = 3

# Ambient noise table
# TODO: Convert to lookup table based on sea_state and scenario.tx_frequency
an = pd.DataFrame({
        1: [34],                # profile at SS1
        2: [39],                # profile at SS2
        3: [47],                # profile at SS3
        4: [50],                # profile at SS4
        5: [52],                # profile at SS5
        6: [54]},               # profile at SS6
        index=[20000])          # frequency of profiles in Hz
