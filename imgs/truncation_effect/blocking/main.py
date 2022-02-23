import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg

lambda_1 = 2
mu = 3
num_of_servers = 3
threshold = 8
seed_num = 1
warm_up_time = 100
num_of_trials = 20
runtime = 10000
# warm_up_time = 10
# num_of_trials = 10
# runtime = 100

all_sim_blocking_times = []
all_markov_blocking_times_low = []
all_markov_blocking_times_mid = []
all_markov_blocking_times_high = []
lambda_2_space = np.linspace(2, 6, 6)
all_capacity_values = (10, 30, 50)
for lambda_2 in lambda_2_space:
    # Simulation
    simulation_results = abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=float("inf"),
        buffer_capacity=float("inf"),
        seed_num=seed_num,
        warm_up_time=warm_up_time,
        num_of_trials=num_of_trials,
        runtime=runtime,
        class_type=None,
    )
    all_sim_blocking_times.append(
        [np.mean(b.blocking_times) for b in simulation_results]
    )

    # Markov
    for capacity_value in all_capacity_values:
        markov_blocking_time = (
            abg.markov.get_mean_blocking_time_using_markov_state_probabilities(
                lambda_2=lambda_2,
                lambda_1=lambda_1,
                mu=mu,
                num_of_servers=num_of_servers,
                threshold=threshold,
                system_capacity=capacity_value,
                buffer_capacity=capacity_value,
            )
        )
        if capacity_value == all_capacity_values[0]:
            all_markov_blocking_times_low.append(markov_blocking_time)
        elif capacity_value == all_capacity_values[1]:
            all_markov_blocking_times_mid.append(markov_blocking_time)
        elif capacity_value == all_capacity_values[2]:
            all_markov_blocking_times_high.append(markov_blocking_time)
        else:
            raise ValueError("Invalid capacity value")

# Waiting time both individuals
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
for index, (ax, all_markov_times) in enumerate(
    zip(
        [ax1, ax2, ax3],
        [
            all_markov_blocking_times_low,
            all_markov_blocking_times_mid,
            all_markov_blocking_times_high,
        ],
    )
):
    ax.violinplot(
        all_sim_blocking_times, positions=lambda_2_space, showmeans=True, widths=0.3
    )
    ax.plot(
        lambda_2_space,
        all_markov_times,
        color="red",
    )
    ax.set_title(f"$N$ = $M$ = {all_capacity_values[index]}")
    ax.legend(["Markov chain", "Simulation"], loc="upper left")
    ax.set_xlabel("$\lambda_2$")
    ax.set_ylabel("Blocking time")

plt.suptitle("Truncation effect on blocking time")
plt.savefig("main.pdf", transparent=True)
