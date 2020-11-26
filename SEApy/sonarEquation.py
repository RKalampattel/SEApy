# sonarEquation.py
#
# Solves the sonar equation for Figure of Merit
#
# Rahul Kalampattel
# Created: 26/11/2020
# Updated: 26/11/2020

import numpy as np

import environment
import scenario


def calculate():

    SL = scenario.tx_source_level

    NSL = environment.an.values[0][environment.sea_state-1]

    f = 0.7*scenario.tx_speed_range*scenario.tx_frequency/1000

    DI = scenario.rx_directivity_index

    DT = scenario.rx_detection_threshold

    FOM = SL - NSL - 10*np.log10(f) + DI - DT

    return FOM
