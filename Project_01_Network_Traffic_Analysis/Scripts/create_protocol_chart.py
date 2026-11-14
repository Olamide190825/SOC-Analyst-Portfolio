import csv
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt

# Locate the project folders
project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "Data" / "sample_traffic.csv"
output_file = project_folder / "Evidence" / "02_protocol_distribution.png"

# Read the simulated traffic dataset
protocol_counts = Counter()

with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        protocol_counts[row["protocol"].strip().upper()] += 1

# Create the chart
protocols = list(protocol_counts.keys())
counts = list(protocol_counts.values())

plt.figure(figsize=(9, 5))
bars = plt.bar(protocols, counts)

plt.title("Network Protocol Distribution")
plt.xlabel("Network Protocol")
plt.ylabel("Number of Records")
plt.suptitle("Simulated dataset — 15 records")

# Display values above each bar
for bar, count in zip(bars, counts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(count),
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.close()

print("Chart created successfully!")
print(f"Saved to: {output_file}")