# main.py
#
# Run SEApy
#
# Rahul Kalampattel
# Created: 23/11/2020
# Updated: 26/11/2020

import transmissionLoss
import sonarEquation

TL = transmissionLoss.calculate(output_flag=False)
print("Transmission loss is: ", round(TL, 1), " dB")

FOM = sonarEquation.calculate()
print("Figure of merit is: ", round(FOM, 1), " dB")

SE = FOM - TL
print("Signal excess is: ", round(SE, 1), " dB")
