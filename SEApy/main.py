# main.py
#
# Rahul Kalampattel
# Created: 23/11/2020
# Updated: 24/11/2020

import transmissionLoss

ss = transmissionLoss.calculate_ss(25, 20)
print("Sound speed is:\t", round(ss, 1))
