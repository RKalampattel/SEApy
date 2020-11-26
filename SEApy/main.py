# main.py
#
# Rahul Kalampattel
# Created: 23/11/2020
# Updated: 24/11/2020

import transmissionLoss

tl_db = transmissionLoss.calculate(output_flag=False)
print("Transmission loss is: ", round(tl_db, 1), " dB")
