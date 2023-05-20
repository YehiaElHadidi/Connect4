import matplotlib.pyplot as plt
import seaborn as sns

depth = ["4", "5", "6", "7", "8"]
avg_time_alpha_beta = [0.023573637, 0.16514492,
                       0.510168314, 2.9393332, 9.912601948]
avg_time_minimax = [0.20680809, 1.604812622,
                    8.279426336, 26.88096261, 139.2105675]


sns.lineplot(x=depth, y=avg_time_alpha_beta, label="Alpha beta pruning")
sns.lineplot(x=depth, y=avg_time_minimax, label="Minimax")

# Set the plot title and labels
plt.title("Average Response Time")
plt.xlabel("Depth Level")
plt.ylabel("Time (s)")
plt.legend()
plt.savefig("response_time.png")

plt.show()
