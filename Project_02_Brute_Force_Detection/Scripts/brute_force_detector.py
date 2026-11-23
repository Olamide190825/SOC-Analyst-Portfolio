
import csv
from datetime import datetime, timedelta
from collections import defaultdict

LOG_FILE = "Data/authentication_log.csv"
THRESHOLD = 5
WINDOW_MINUTES = 5

events = defaultdict(list)

# Read authentication records
with open(LOG_FILE, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        timestamp = datetime.strptime(
            row["timestamp"], "%Y-%m-%d %H:%M:%S"
        )

        key = (row["username"], row["source_ip"])

        events[key].append({
            "timestamp": timestamp,
            "status": row["status"]
        })

print("BRUTE-FORCE DETECTION REPORT")
print("=" * 45)

# Investigate each account and source IP
for (username, source_ip), records in events.items():

    records.sort(key=lambda event: event["timestamp"])

    failures = [
        event for event in records
        if event["status"] == "FAILED"
    ]

    successes = [
        event for event in records
        if event["status"] == "SUCCESS"
    ]

    alert_found = False

    # Examine rolling five-minute windows
    for start_event in failures:

        window_end = start_event["timestamp"] + timedelta(
            minutes=WINDOW_MINUTES
        )

        window_failures = [
            event for event in failures
            if start_event["timestamp"]
            <= event["timestamp"] <= window_end
        ]

        if len(window_failures) >= THRESHOLD:

            # Identify the fifth failed login
            fifth_failure = window_failures[THRESHOLD - 1]

            # Check for success AFTER the fifth failure
            successful_after = [
                event for event in successes
                if fifth_failure["timestamp"]
                < event["timestamp"] <= window_end
            ]

            print("\nALERT: Possible brute-force activity")
            print(f"Username: {username}")
            print(f"Source IP: {source_ip}")
            print(f"Failed attempts in window: {len(window_failures)}")
            print(
                "Fifth failed login:",
                fifth_failure["timestamp"]
            )

            if successful_after:
                print("Successful login AFTER fifth failure: YES")

                for event in successful_after:
                    print("Successful login time:", event["timestamp"])
            else:
                print("Successful login AFTER fifth failure: NO")

            alert_found = True
            break

    if not alert_found:
        print(
            f"\nNo brute-force alert for {username} "
            f"from {source_ip}"
        )
