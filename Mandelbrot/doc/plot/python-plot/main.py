import matplotlib.pyplot as plt

# Neue Szenarien mit 1 bis 4 Workern
scenarios = ["1 Worker", "2 Workers", "3 Workers", "4 Workers"]
times_ms = [30920, 15613, 10572, 8212]

# Neue Chunk-Verteilungen entsprechend der Zusammenfassungen
chunk_distribution = [
    {"worker_1": 1200},
    {"worker_1": 604, "worker_4": 596},
    {"worker_1": 390, "worker_2": 409, "worker_4": 401},
    {"worker_1": 297, "worker_2": 296, "worker_3": 296, "worker_4": 311}
]

# Farben für konsistente Darstellung
worker_labels = ["worker_1", "worker_2", "worker_3", "worker_4"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Diagramm erstellen
plt.figure(figsize=(12, 6))

# Subplot 1: Verarbeitungszeit
plt.subplot(1, 2, 1)
plt.bar(scenarios, times_ms, color="skyblue")
plt.title("Processing Time per Scenario")
plt.ylabel("Time (ms)")
plt.xlabel("Worker Configuration")

# Subplot 2: Chunk-Verteilung (gestapelt)
plt.subplot(1, 2, 2)

width = 0.6
bottom = [0] * len(scenarios)

for i, worker in enumerate(worker_labels):
    data = [config.get(worker, 0) for config in chunk_distribution]
    plt.bar(scenarios, data, width, bottom=bottom, label=worker, color=colors[i])
    bottom = [sum(x) for x in zip(bottom, data)]

plt.title("Chunk Distribution per Worker")
plt.ylabel("Chunks Processed")
plt.xlabel("Worker Configuration")
plt.legend()

plt.tight_layout()
plt.show()
