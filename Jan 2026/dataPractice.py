# data = input("This will come from STDIN: ")
# print("Now we write it to STDOUT: " + data)
# print("Now we generate an error to STDERR: " + data + 1)

# ./streams.py 
""" This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks! """

""" cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z """


""" echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cat variables.py
#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
./variables.py 
export FRUIT=Pineapple
./variables.py  """


""" import os
import subprocess

my_env = os.environ.copy() #dic with env variables
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env) """

""" import re
def show_time_of_pid(line):
  pattern =r"([A-Za-z]+\s\d+\s\d+:\d+:\d+).*?\[(\d+)\]"
  result = re.search(pattern, line)
  return f'{result[1]} pid:{result[2]}'

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440 """




""" #!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)

    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1

print(usernames) """





#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
  error = input("What is the error?")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
        for i in range(len(error.split(' '))):
            client_loop: send disconnect: I/O errorappend(r"{}".format(error.split(' ')[i].lower()))
        if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
            returned_errors.append(log)
  file.close()
  return returned_errors


def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
      for error in returned_errors:
          file.write(error)
  file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)
