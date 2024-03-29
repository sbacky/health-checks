#! usr/bin/env python3

import psutil
import shutil
import os

def cpu_usage():
    """Returns CPU usage as percentage as string"""
    # Getting loadover15 minutes
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load15/os.cpu_count()) * 100
    return f'The CPU usage is : {cpu_usage}'

def ram_usage():
    """Returns RAM usage as percentage as string"""
    # Getting % usage of virtual_memory ( 3rd field)
    return f'RAM memory % used: {psutil.virtual_memory()[2]}'

def storage_usage():
    """Returns Storage usage as percetage as string"""
    du = shutil.disk_usage("/")
    # Calculate the percentage of free space
    percent_used = 100 * du.used / du.total
    gb_used = du.used / 2**30
    percent_free = 100 * du.free / du.total
    gb_free = du.free / 2**30
    total_gb = du.total / 2**30
    return f'Storage % used: {percent_used}\nGB Used: {gb_used} gb\n\nStorage % free: {percent_free}\nGB Free: {gb_free} gb\n\nTotal GB: {total_gb} gb'

def main():
    vitals = [
        cpu_usage,
        ram_usage,
        storage_usage,
    ]
    print("\n")
    for vital in vitals:
        print(vital())
        print("-" * 10)

main()