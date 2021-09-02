import numpy as np
import ambulance_game as abg

lambda_1 = 2
lambda_2 = 3
mu = 1
num_of_servers = 6
threshold = 10
system_capacity = 20
buffer_capacity = 10
target = 1

Simulation = abg.simulation.simulate_model(
    lambda_2=lambda_2,
    lambda_1=lambda_1,
    mu=mu,
    num_of_servers=num_of_servers,
    threshold=threshold,
    system_capacity=system_capacity,
    buffer_capacity=buffer_capacity,
    seed_num=0,
    runtime=2000,
)

mean_wait = np.mean([w.waiting_time for w in Simulation.get_all_records()])
mean_block = np.mean([b.time_blocked for b in Simulation.get_all_records()])
mean_service = np.mean([s.service_time for s in Simulation.get_all_records()])
proportion_within_target = np.mean(
    [1 if w.waiting_time <= target else 0 for w in Simulation.get_all_records()]
)
