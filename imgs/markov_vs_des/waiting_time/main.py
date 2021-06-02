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
seed_num = 0
warm_up_time = 500
num_of_trials = 100
runtime = 100000


simulation_results_overall = abg.simulation.get_multiple_runs_results(
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

simulation_results_type_1 = abg.simulation.get_multiple_runs_results(
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

simulation_results_type_2 = abg.simulation.get_multiple_runs_results(
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

waiting_times_simulation_overall = [
    np.mean(w.waiting_times) for w in simulation_results_overall
]
waiting_times_simulation_type_1 = [
    np.mean(w.waiting_times) for w in simulation_results_type_1
]
waiting_times_simulation_type_2 = [
    np.mean(w.waiting_times) for w in simulation_results_type_2
]


mean_waiting_time_markov_overall = (
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

mean_waiting_time_markov_type_1 = (
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

mean_waiting_time_markov_type_2 = (
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


labels = ["Type 1", "Type 2", "Overall"]
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    [
        waiting_times_simulation_type_1,
        waiting_times_simulation_type_2,
        waiting_times_simulation_overall,
    ],
    showmeans=True,
    showmedians=False,
)
ax.plot(
    [0.85, 1.15],
    [mean_waiting_time_markov_type_1, mean_waiting_time_markov_type_1],
    color="red",
)
ax.legend(["Markov chain", "Simulation"])
ax.plot(
    [1.85, 2.15],
    [mean_waiting_time_markov_type_2, mean_waiting_time_markov_type_2],
    color="red",
)
ax.plot(
    [2.85, 3.15],
    [mean_waiting_time_markov_overall, mean_waiting_time_markov_overall],
    color="red",
)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(labels)
ax.set_title("Waiting time")

plt.savefig("main.pdf", transparent=True)
