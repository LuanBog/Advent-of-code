#!/usr/bin/env python

from os import startfile
import time

begin_time = time.time()

class Simulation:
    def __init__(self, crabs, position_to_align_to):
        self.crabs = crabs
        self.position_to_align_to = position_to_align_to
        self.fuel_cost = 0

        self.run()

    def run(self):
        for index, crab in enumerate(self.crabs):
            fuel_burn_rate = 1

            while self.crabs[index] != self.position_to_align_to:
                self.fuel_cost += fuel_burn_rate
                fuel_burn_rate += 1

                if crab > self.position_to_align_to:
                    self.crabs[index] -= 1
                elif crab < self.position_to_align_to:
                    self.crabs[index] += 1

with open('./data.txt', 'r') as file:
    crabs = [int(i) for i in file.read().strip().split(',')]

# Run the simulation
simulations = []

for i in range(max(crabs) + 1):
    crab_data = crabs.copy()
    simulation = Simulation(crab_data, i)
    simulations.append({'position': i, 'fuel': simulation.fuel_cost})

    print('Simulation: {} / {} (Fuel: {})'.format(i, max(crabs), simulation.fuel_cost))

sorted_simulations = sorted(simulations, key=lambda x: x['fuel'])

print('\n--------------- RESULT ---------------')
print('(Least) Fuel: {}, Position: {}'.format(sorted_simulations[0]['fuel'], sorted_simulations[0]['position']))
print('(Most) Fuel: {}, Position: {}'.format(sorted_simulations[-1]['fuel'], sorted_simulations[-1]['position']))

print('\nExecution time: {} seconds'.format(time.time() - begin_time))
