import numpy as np
import ambulance_game as abg

(
    overall_proportion,
    class_1_proportion,
    class_2_proportion,
) = abg.simulation.get_mean_proportion_of_individuals_within_target_for_multiple_runs(
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
    target=1,
)
