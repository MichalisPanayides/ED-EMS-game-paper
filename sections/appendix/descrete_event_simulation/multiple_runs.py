import numpy as np
import ambulance_game as abg

all_simulations = abg.simulation.get_multiple_runs_results(
    lambda_1=3,
    lambda_2=2,
    mu=1,
    num_of_servers=6,
    threshold=10,
    system_capacity=20,
    buffer_capacity=10,
    seed_num=0,
    runtime=2000,
    num_of_trials=10,
)

all_waits = [np.mean(w.waiting_times) for w in all_simulations]
all_services = [np.mean(s.service_times) for s in mult_results]
all_blocks = [np.mean(b.blocking_times) for b in mult_results]

mean_wait = np.mean(all_waits)
mean_service = np.mean(all_services)
mean_block = np.mean(all_blocks)
