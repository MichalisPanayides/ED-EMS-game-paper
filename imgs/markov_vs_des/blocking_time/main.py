import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg

lambda_2 = 3
lambda_1 = 4
mu = 8
num_of_servers = 1
threshold = 8
system_capacity = 10
buffer_capacity = 10
seed_num = None
warm_up_time = 500
num_of_trials = 100
runtime = 100000


simulation_results = abg.simulation.get_multiple_runs_results(
    lambda_2=lambda_2,
    lambda_1=lambda_1,
    mu=mu,
    num_of_servers=num_of_servers,
    threshold=threshold,
    system_capacity=system_capacity,
    buffer_capacity=buffer_capacity,
    seed_num=seed_num,
    warm_up_time=warm_up_time,
    num_of_trials=num_of_trials,
    runtime=runtime,
    class_type=1,
)

blocking_times_simulation = [np.mean(b.blocking_times) for b in simulation_results]

mean_blocking_time_markov = (
    abg.markov.get_mean_blocking_time_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=system_capacity,
        buffer_capacity=buffer_capacity,
    )
)


fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    blocking_times_simulation,
    showmeans=True,
)
ax.plot(
    [0.85, 1.15],
    [mean_blocking_time_markov, mean_blocking_time_markov],
    color="red",
)
ax.set_xticks([1])
ax.set_xticklabels(["Type 2 individuals"])
ax.set_title("Blocking time")
ax.legend(["Markov chain", "Simulation"])

plt.savefig("main.pdf", transparent=True)
