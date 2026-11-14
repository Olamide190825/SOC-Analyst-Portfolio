import csv
from collections import Counter
from pathlib import Path

# Locate the sample network traffic file
project_folder = Path(__file__).resolve().parent.parent
data_file = project_folder / "Data" / "sample_traffic.csv"

protocol_counts = Counter()
source_counts = Counter()
destination_counts = Counter()
total_packets = 0

if not data_file.exists():
    print(f"Sample data file not found: {data_file}")
    raise SystemExit(1)

with data_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    required_columns = {
        "timestamp",
        "source_ip",
        "destination_ip",
        "protocol",
        "size_bytes"
    }

    if not required_columns.issubset(reader.fieldnames or []):
        print("The CSV file is missing required columns.")
        raise SystemExit(1)

    for row in reader:
        protocol = row["protocol"].strip().upper()
        source_ip = row["source_ip"].strip()
        destination_ip = row["destination_ip"].strip()

        protocol_counts[protocol] += 1
        source_counts[source_ip] += 1
        destination_counts[destination_ip] += 1
        total_packets += 1

print("\n========== NETWORK TRAFFIC ANALYSIS ==========")
print(f"Total packets analysed: {total_packets}")

print("\nProtocol distribution:")
for protocol, count in protocol_counts.most_common():
    print(f"{protocol}: {count}")

print("\nTop source IP addresses:")
for ip, count in source_counts.most_common(5):
    print(f"{ip}: {count} packets")

print("\nTop destination IP addresses:")
for ip, count in destination_counts.most_common(5):
    print(f"{ip}: {count} packets")

print("\nAnalysis completed.")