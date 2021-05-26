import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg

lambda_1 = 4
mu = 3
num_of_servers = 3
threshold = 8
system_capacity = 10
buffer_capacity = 10
target = 0.5
seed_num = None
warm_up_time = 500
num_of_trials = 100
runtime = 10000
# warm_up_time = 10
# num_of_trials = 10
# runtime = 100

all_sim_prop_1 = []
all_sim_prop_2 = []
all_sim_prop_overall = []

all_markov_prop_1 = []
all_markov_prop_2 = []
all_markov_prop_overall = []
lambda_2_space = np.linspace(2, 6, 6)
for lambda_2 in lambda_2_space:
    # Simulation
    (
        sim_prop_overall,
        sim_prop_1,
        sim_prop_2,
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
    all_sim_prop_overall.append(sim_prop_overall)
    all_sim_prop_1.append(sim_prop_1)
    all_sim_prop_2.append(sim_prop_2)

    # Markov - type 1
    markov_prop_1 = (
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
    all_markov_prop_1.append(markov_prop_1)

    # Markov - type 2
    markov_prop_2 = (
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
    all_markov_prop_2.append(markov_prop_2)

    # Markov - overall
    markov_prop_overall = (
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
    all_markov_prop_overall.append(markov_prop_overall)


# Proportion type 1
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(all_sim_prop_1, positions=lambda_2_space, showmeans=True, widths=0.3)
ax.plot(
    lambda_2_space,
    all_markov_prop_1,
    color="red",
)
ax.set_title("Proportion of type 1 individuals within target")
ax.legend(["Markov chain", "Simulation"])
ax.set_xlabel("$\lambda_2$")
ax.set_ylabel("Proportion")

plt.savefig("proportion_1.pdf", transparent=True)


# Proportion type 2
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(all_sim_prop_2, positions=lambda_2_space, showmeans=True, widths=0.3)
ax.plot(
    lambda_2_space,
    all_markov_prop_2,
    color="red",
)
ax.set_title("Proportion of type 2 individuals within target")
ax.legend(["Markov chain", "Simulation"])
ax.set_xlabel("$\lambda_2$")
ax.set_ylabel("Proportion")

plt.savefig("proportion_2.pdf", transparent=True)


# Proportion overall
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.violinplot(
    all_sim_prop_overall, positions=lambda_2_space, showmeans=True, widths=0.3
)
ax.plot(
    lambda_2_space,
    all_markov_prop_overall,
    color="red",
)
ax.set_title("Overall proportion individuals within target")
ax.legend(["Markov chain", "Simulation"])
ax.set_xlabel("$\lambda_2$")
ax.set_ylabel("Proportion")

plt.savefig("proportion_overall.pdf", transparent=True)
