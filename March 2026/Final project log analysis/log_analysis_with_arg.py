#!/usr/bin/env python3

import re
import csv
import argparse


def main():

    parser = argparse.ArgumentParser(description="Analyze syslog logs")
    parser.add_argument("logfile", help="Path to the syslog log file")

    args = parser.parse_args()
    log_file = args.logfile

    error_counts = {}
    user_stats = {}

    with open(log_file) as f:
        for line in f:

            match_error = re.search(r"ticky: ERROR (.*)\((.*)\)", line)
            if match_error:
                error_message = match_error.group(1).strip()

                if error_message not in error_counts:
                    error_counts[error_message] = 0

                error_counts[error_message] += 1

            match_user = re.search(r"(ERROR|INFO)(.*)\((.*)\)", line)
            if match_user:
                user = match_user.group(3)
                log_type = match_user.group(1)

                if user not in user_stats:
                    user_stats[user] = {"INFO": 0, "ERROR": 0}

                user_stats[user][log_type] += 1

    sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
    sorted_users = sorted(user_stats.items())

    with open("error_message.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Error", "Count"])

        for error, count in sorted_errors:
            writer.writerow([error, count])

    with open("user_statistics.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Username", "INFO", "ERROR"])

        for user, stats in sorted_users:
            writer.writerow([user, stats["INFO"], stats["ERROR"]])


if __name__ == "__main__":
    main()