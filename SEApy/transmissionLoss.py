# transmissionLoss.py
#
# Rahul Kalampattel
# Created: 24/11/2020
# Updated: 24/11/2020

import arlpy.uwapm as uwapm
import arlpy.uwa as uwa

env = uwapm.create_env2d()


def calculate_ss(t, d):
    ss = uwa.soundspeed(temperature=t, depth=d)
    return ss
