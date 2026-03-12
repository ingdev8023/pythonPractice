mkdir mynewdir
cd mynewdir/
/mynewdir$ pwd
/mynewdir$ cp ../spider.txt .
/mynewdir$ touch myfile.txt
/mynewdir$ ls -l 
#Output:
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 myfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
/mynewdir$ ls -la
#Output:
#total 12
#drwxr-xr-x  2 user user  4096 Mai 22 14:17 .
#drwxr-xr-x 56 user user 12288 Mai 22 14:17 ..
#-rw-rw-r--  1 user user     0 Mai 22 14:22 myfile.txt
#-rw-rw-r--  1 user user   192 Mai 22 14:18 spider.txt
/mynewdir$ mv myfile.txt emptyfile.txt
/mynewdir$ cp spider.txt yetanotherfile.txt
/mynewdir$ ls -l
#Output:
#total 8
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 emptyfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:23 yetanotherfile.txt
/mynewdir$ rm *
/mynewdir$ ls -l
#total 0
/mynewdir$ cd ..
rmdir mynewdir/
ls mynewdir
#ls: cannot access 'mynewdir': No such file or directory






cat stdout_example.py 
#!/usr/bin/env python3
print("Don't mind me, just a bit of text here...")
./stdout_example.py 
#Output: Don't mind me, just a bit of text here...
./stdout_example.py > new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
./stdout_example.py >> new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
 #Don't mind me, just a bit of text here...
cat streams_err.py 
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
./streams_err.py < new_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
./streams_err.py < new_file.txt 2> error_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
cat error_file.txt 
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
echo "These are the contents of the file" > myamazingfile.txt
cat myamazingfile.txt 
#These are the contents of the file




ls -l | less
#(... A list of files appears...)
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
     # 7 the
     # 3 up
     # 3 spider
     # 3 and
     # 2 rain
     # 2 itsy
     # 2 climbed
     # 2 came
     # 2 bitsy
     # 1 waterspout.


cat haiku.txt 
#advance your career,
#automating with Python,
#it's so fun to learn.



cat capitalize.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())



cat haiku.txt | ./capitalize.py 
#Advance your career,
#Automating with python,
#It's so fun to learn.



./capitalize.py < haiku.txt
#Advance your career,
#Automating with python,
#It's so fun to learn.



#!/bin/bash
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"



#!/bin/bash

echo "Starting at: $(date)"; echo


echo "UPTIME"; uptime;echo

echo "FREE";free; echo

echo "WHO";who;echo

echo "Finishing at: $(date)"


if [ -n "$PATH" ];then echo "your path is not empty"; fi

if test -n "$PATH";then echo "your path is not empty"; fi


n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done

#using PYTHON
import sys
import random

value = random.randint(0, 3)
print("Returning: " + str(value))
sys.exit(value)


#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;

#review command basename

#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
        echo mv "$file" "$name.html" 
done


