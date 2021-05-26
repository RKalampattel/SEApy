# transmissionLoss.py
#
# Calculates transmission loss in dB
#
# Rahul Kalampattel
# Created: 24/11/2020
# Updated: 27/11/2020
# Jay Patel
# Updated: 26/05/2021

import arlpy.uwapm as pm
import numpy as np

import environment
import scenario


def calculate(output_flag):
    # Set up environment
    env = pm.create_env2d(
        bottom_absorption=environment.bottom_absorption,
        bottom_density=environment.bottom_density,
        depth=environment.depth,
        soundspeed=environment.ssp,
        surface=environment.surface,
        rx_depth=scenario.rx_depth,
        rx_range=scenario.rx_range,
        tx_depth=scenario.tx_depth,
        tx_directionality=scenario.tx_beampattern
    )

    # Propagate rays and calculate transmission loss
    rays = pm.compute_eigenrays(env, model='bellhop')

    arrivals = pm.compute_arrivals(env,  model='bellhop')

    tl = pm.compute_transmission_loss(env, model='bellhop')

    # Convert transmission loss to dB
    tl_db = np.abs(20*np.log10(np.abs(tl.iloc[0, 0])))

    # Generate plots and other output
    if output_flag:
        pm.print_env(env)

        pm.plot_env(env, width=1000)

        pm.plot_ssp(env, width=1000)

        # You need to again calculate rays first, previously you only calculated the eigen rays. 
        rays = pm.compute_rays(env)
        pm.plot_rays(rays, env=env, width=1000)

        pm.plot_arrivals(arrivals, dB=True, width=1000)

        print(arrivals[arrivals.arrival_number < 10]
              [['time_of_arrival', 'arrival_amplitude',
                'surface_bounces', 'bottom_bounces']])

        env['rx_range'] = np.linspace(0, scenario.rx_range+100, 1+5*(scenario.rx_range+100))
        env['rx_depth'] = np.linspace(0, environment.depth, 1+5*environment.depth)

        tl = pm.compute_transmission_loss(env, model='bellhop')

        pm.plot_transmission_loss(tl, env=env, clim=[-60, 10], width=1000)

        tl.to_csv("transmissionLossRaw.csv")

    return tl_db
