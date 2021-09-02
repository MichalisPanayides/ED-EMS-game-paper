import numpy as np
import ambulance_game as abg

Simulation = abg.simulation.simulate_model(
    lambda_1=3,
    lambda_2=2,
    mu=1,
    num_of_servers=6,
    threshold=10,
    system_capacity=20,
    buffer_capacity=10,
    seed_num=0,
    runtime=2000,
)

mean_wait = np.mean([w.waiting_time for w in Simulation.get_all_records()])

mean_block = np.mean([b.time_blocked for b in Simulation.get_all_records()])

mean_service = np.mean([s.service_time for s in Simulation.get_all_records()])

target = 1
proportion_within_target = np.mean(
    [1 if w.waiting_time <= target else 0 for w in Simulation.get_all_records()]
)
