import os
import datetime
import platform
import psutil

# -------------------------------------
# script for fetching the top process in the windows system ########
#check os information
#display the OS type -windows/Linux

#define CPU threshold
#check the CPU utilization
# if utilization is greater than threshold, 
    # create log file & print the current CPU value with DATE & TIME
#else:
#display CPU utilization on the terminal
#---------------------------------------------------

#get OS details
os_name = platform.system()
os_version = platform.release()
#os_platform = platform.platform()
user_logged_in = psutil.users()
#print(type(user_logged_in))
print(f"Hello {user_logged_in[0][0]}!!!. The HOST is {os_name} {os_version} version")

cpu_threshold = 5

#check current CPU utilization
current_cpu = psutil.cpu_percent(interval=1)
print(current_cpu, "%")

try:
    if (cpu_threshold < int(current_cpu)):
        date_time = datetime.datetime.now()
        formatted_datetime = date_time.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{formatted_datetime}.txt"
        with open(file_name, 'w') as f:
            f.write(f'The time is {formatted_datetime} and current CPU is {current_cpu}%')
    else:
        print(f"This is the current CPU value {current_cpu}% and its below threshold {cpu_threshold}%")
        
except FileNotFoundError or PermissionError:
    print('unable to create file!!')
