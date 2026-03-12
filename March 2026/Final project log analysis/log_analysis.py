#!/usr/bin/env python3

import re
import sys
import csv

#first step receiving the log

log_file = sys.argv[1]
error_counts = {}
user_stats = {}
#opening the file 

with open(log_file) as f:
    for line in f:
#using ReGex for log analysis.
#re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        match_error =re.search(r"ticky: ERROR (.*)\((.*)\)", line)
        if match_error:
            error_message = match_error.group(1)
           
            if error_message not in error_counts:
                error_counts[error_message] = 0
            
            error_counts[error_message] += 1
        
        match_user = re.search(r"(ERROR|INFO)(.*)\((.*)\)",line)
        user = match_user.group(3)
        log_type = match_user.group(1)
        if user not in user_stats:
                user_stats[user] = {"INFO":0, "ERROR":0}
        user_stats[user][log_type] += 1
#sorting the dict
sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
sorted_users = sorted(user_stats.items())

#now the csv

with open("error_message.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Error", "Count"])

    for error, count in sorted_errors:
        writer.writerow([error, count])

with open("user_statistics.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Username", "INFO", "ERROR"])

    for user, stats in sorted_users:
        writer.writerow([user, stats["INFO"], stats["ERROR"]])
