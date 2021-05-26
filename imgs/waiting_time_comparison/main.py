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

all_sim_waiting_times_1 = []
all_sim_waiting_times_2 = []
all_sim_waiting_times_all = []

all_markov_waiting_times_1 = []
all_markov_waiting_times_2 = []
all_markov_waiting_times_all = []
lambda_2_space = np.linspace(2, 6, 6)
for lambda_2 in lambda_2_space:
    # Simulation - type 1
    simulation_results_1 = abg.simulation.get_multiple_runs_results(
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
        class_type=0,
    )
    all_sim_waiting_times_1.append(
        [np.mean(w.waiting_times) for w in simulation_results_1]
    )

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
    all_sim_waiting_times_2.append(
        [np.mean(w.waiting_times) for w in simulation_results_2]
    )

    # Simulation - overall
    simulation_results_all = abg.simulation.get_multiple_runs_results(
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
        class_type=None,
    )
    all_sim_waiting_times_all.append(
        [np.mean(w.waiting_times) for w in simulation_results_all]
    )

    # Markov - type 1
    markov_waiting_value_1 = (
        abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
            lambda_2=lambda_2,
            lambda_1=lambda_1,
            mu=mu,
            num_of_servers=num_of_servers,
            threshold=threshold,
            system_capacity=system_capacity,
            buffer_capacity=buffer_capacity,
            class_type=0,
        )
    )
    all_markov_waiting_times_1.append(markov_waiting_value_1)

    # Markov - type 2
    markov_waiting_value_2 = (
        abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
            lambda_2=lambda_2,
            lambda_1=lambda_1,
            mu=mu,
            num_of_servers=num_of_servers,
            threshold=threshold,
            system_capacity=system_capacity,
            buffer_capacity=buffer_capacity,
            class_type=1,
        )
    )
    all_markov_waiting_times_2.append(markov_waiting_value_2)

    # Markov - overall
    markov_waiting_value_all = (
        abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
            lambda_2=lambda_2,
            lambda_1=lambda_1,
            mu=mu,
            num_of_servers=num_of_servers,
            threshold=threshold,
            system_capacity=system_capacity,
            buffer_capacity=buffer_capacity,
            class_type=None,
        )
    )
    all_markov_waiting_times_all.append(markov_waiting_value_all)


# Waiting time type 1 individuals
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    all_sim_waiting_times_1, positions=lambda_2_space, showmeans=True, widths=0.3
)
ax.plot(
    lambda_2_space,
    all_markov_waiting_times_1,
    color="red",
)
ax.set_title(
    "Mean waiting time of type 1 individuals using Markov chain and simulation"
)
ax.legend(["Markov chain", "Simulation"])
ax.set_xlabel("$\lambda_2$")
ax.set_ylabel("Waiting time")

plt.savefig("waiting_1.pdf", transparent=True)


# Waiting time type 2 individuals
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    all_sim_waiting_times_2, positions=lambda_2_space, showmeans=True, widths=0.3
)
ax.plot(
    lambda_2_space,
    all_markov_waiting_times_2,
    color="red",
)
ax.set_title(
    "Mean waiting time of type 2 individuals using Markov chain and simulation"
)
ax.legend(["Markov chain", "Simulation"])
ax.set_xlabel("$\lambda_2$")
ax.set_ylabel("Waiting time")

plt.savefig("waiting_2.pdf", transparent=True)


# Waiting time both individuals
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    all_sim_waiting_times_all, positions=lambda_2_space, showmeans=True, widths=0.3
)
ax.plot(
    lambda_2_space,
    all_markov_waiting_times_all,
    color="red",
)
ax.set_title("Overall mean waiting time using Markov chain and simulation")
ax.legend(["Markov chain", "Simulation"])
ax.set_xlabel("$\lambda_2$")
ax.set_ylabel("Waiting time")

plt.savefig("waiting_overall.pdf", transparent=True)
