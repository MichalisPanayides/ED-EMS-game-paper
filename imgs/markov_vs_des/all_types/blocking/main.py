import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg

lambda_1 = 4
mu = 3
num_of_servers = 3
threshold = 8
system_capacity = 10
buffer_capacity = 10
seed_num = None
warm_up_time = 500
num_of_trials = 100
runtime = 10000
# warm_up_time = 10
# num_of_trials = 10
# runtime = 100

all_sim_blocking_times_2 = []
all_markov_blocking_times_2 = []
lambda_2_space = np.linspace(2, 6, 6)
for lambda_2 in lambda_2_space:
    # Simulation - type 2
    simulation_results_2 = abg.simulation.get_multiple_runs_results(
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
    all_sim_blocking_times_2.append(
        [np.mean(b.blocking_times) for b in simulation_results_2]
    )

    # Markov - type 2
    markov_blocking_value_2 = (
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
    all_markov_blocking_times_2.append(markov_blocking_value_2)


# Blocking time type 2 individuals
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    all_sim_blocking_times_2, positions=lambda_2_space, showmeans=True, widths=0.3
)
ax.plot(
    lambda_2_space,
    all_markov_blocking_times_2,
    color="red",
)
ax.set_title("Blocking time using Markov chain and simulation")
ax.legend(["Markov chain", "Simulation"])
ax.set_xlabel("$\lambda_2$")
ax.set_ylabel("Time blocked")

plt.savefig("blocking.pdf", transparent=True)
