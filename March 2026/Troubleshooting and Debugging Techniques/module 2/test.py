import psutil
psutil.cpu_percent()
# using psutil.disk_io_counters() and psutil.net_io_counters() you'll get byte read and byte write for disk I/O and byte received and byte sent for the network I/O bandwidth. For checking disk I/O, you can use the following command:
psutil.disk_io_counters()
psutil.net_io_counters()