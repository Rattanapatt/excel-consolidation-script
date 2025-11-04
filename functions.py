import os
import time

# Function to check if a template file exists in the 'templates' directory
def check_template_exists():
    overall_path = os.path.join('templates.xlsx') # Checking in the current directory for simplicity
    with open('execute_log.txt', 'a') as f: # Log file to record the check
        if os.path.isfile(overall_path):
            f.write("Template file exists.\n")
        else:
            f.write("Template file does not exist.\n")
    return os.path.isfile(overall_path)

# Function to get the current execution time
def execute_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # Format: YYYY-MM-DD HH:MM:SS

# Function to log the execution time in a header format
def header_log(execute_time):
    with open('execute_log.txt', 'a') as f: # Log file to record the execution time
        f.write("----- Execution Log -----\n")
        f.write(f"Execution Time: {execute_time}\n")
    return

# Function to clear the log file
def clear_log_file(filename='execute_log.txt'):
    with open(filename, 'w') as f:
        pass
    print(f"Log file '{filename}' has been cleared.")