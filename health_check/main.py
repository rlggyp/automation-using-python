#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  usage = du.used / du.total * 100
  return usage

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage

disk_usage = check_disk_usage("/")
cpu_usage = check_cpu_usage()

if disk_usage > 80: # if disk usage > 80%
  print("Warning! CPU Usage: {:>4.1f}%".format(disk_usage))
elif cpu_usage > 80:  # cpu usage > 80%
  print("Warning! Disk Usage: {:>4.1f}%".format(cpu_usage))
else:
  print("Everything is OK!")
