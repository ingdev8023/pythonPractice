import sys
import re

log_file = sys.argv[1]

with open(log_file) as f:
    for line in f:
        match_error = re.search(r"ticky: ERROR (.*)\((.*)\)", line)
        if match_error:
            message = match_error.group(1).strip()
            user = match_error.group(2)
            print(f"ERROR | {user} | {message}")

            
