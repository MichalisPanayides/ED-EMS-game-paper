import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg

lambda_2 = 3
lambda_1 = 4
mu = 8
num_of_servers = 1
threshold = 8
target = 0.5
system_capacity = 10
buffer_capacity = 10
seed_num = None
warm_up_time = 500
num_of_trials = 100
runtime = 100000


(
    simulation_results_overall,
    simulation_results_type_1,
    simulation_results_type_2,
) = abg.simulation.get_mean_proportion_of_individuals_within_target_for_multiple_runs(
    lambda_2=lambda_2,
    lambda_1=lambda_1,
    mu=mu,
    num_of_servers=num_of_servers,
    threshold=threshold,
    system_capacity=system_capacity,
    buffer_capacity=buffer_capacity,
    seed_num=seed_num,
    num_of_trials=num_of_trials,
    runtime=runtime,
    target=target,
)

mean_proportion_markov_overall = (
    abg.markov.proportion_within_target_using_markov_state_probabilities(
        lambda_1=lambda_1,
        lambda_2=lambda_2,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=system_capacity,
        buffer_capacity=buffer_capacity,
        target=target,
        class_type=None,
    )
)

mean_proportion_markov_type_1 = (
    abg.markov.proportion_within_target_using_markov_state_probabilities(
        lambda_1=lambda_1,
        lambda_2=lambda_2,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=system_capacity,
        buffer_capacity=buffer_capacity,
        target=target,
        class_type=0,
    )
)

mean_proportion_markov_type_2 = (
    abg.markov.proportion_within_target_using_markov_state_probabilities(
        lambda_1=lambda_1,
        lambda_2=lambda_2,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=system_capacity,
        buffer_capacity=buffer_capacity,
        target=target,
        class_type=1,
    )
)


labels = ["Type 1", "Type 2", "Overall"]
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    [
        simulation_results_type_1,
        simulation_results_type_2,
        simulation_results_overall,
    ],
    showmeans=True,
)
ax.plot(
    [0.85, 1.15],
    [mean_proportion_markov_type_1, mean_proportion_markov_type_1],
    color="red",
)
ax.legend(["Markov chain", "Simulation"])
ax.plot(
    [1.85, 2.15],
    [mean_proportion_markov_type_2, mean_proportion_markov_type_2],
    color="red",
)
ax.plot(
    [2.85, 3.15],
    [mean_proportion_markov_overall, mean_proportion_markov_overall],
    color="red",
)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(labels)
ax.set_title("Proportion of individuals within time")

plt.savefig("main.pdf", transparent=True)
