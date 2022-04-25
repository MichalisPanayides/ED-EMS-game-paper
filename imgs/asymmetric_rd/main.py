import nashpy as nash
import numpy as np
import matplotlib.pyplot as plt

import ambulance_game as abg

lambda_2 = 2
lambda_1_1 = 1
lambda_1_2 = 2
mu_1 = 2
mu_2 = 2.5
num_of_servers_1 = 2
num_of_servers_2 = 2
system_capacity_1 = 10
system_capacity_2 = 10
buffer_capacity_1 = 6
buffer_capacity_2 = 6
target = 2
alpha = 0.5


A, B, R = abg.game.get_payoff_matrices(
    lambda_2=lambda_2,
    lambda_1_1=lambda_1_1,
    lambda_1_2=lambda_1_2,
    mu_1=mu_1,
    mu_2=mu_2,
    num_of_servers_1=num_of_servers_1,
    num_of_servers_2=num_of_servers_2,
    system_capacity_1=system_capacity_1,
    system_capacity_2=system_capacity_2,
    buffer_capacity_1=buffer_capacity_1,
    buffer_capacity_2=buffer_capacity_2,
    target=target,
    alpha=alpha,
)
A += 1
B += 1

my_game = nash.Game(A, B)
xs, ys = my_game.asymmetric_replicator_dynamics(timepoints=np.linspace(1, 200000, 100))

plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.plot(xs)
plt.xlabel("Timepoints")
plt.ylabel("Probability")
plt.title("Hospital A")
plt.legend([f"$s_{{{i + 1}}}$" for i in range(len(xs[0]))])

plt.subplot(1, 2, 2)
plt.plot(ys)
plt.xlabel("Timepoints")
plt.ylabel("Probability")
plt.title("Hospital B")
plt.legend([f"$s_{{{i + 1}}}$" for i in range(len(ys[0]))])

plt.savefig("asymmetric_rd_2.png", transparent=True)
