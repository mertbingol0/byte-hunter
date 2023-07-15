import os
import subprocess
from datetime import datetime

log_file = 'command_log.txt'

def console_log():

    def log_command(command):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        with open(log_file, 'a') as file:
            file.write(f'{current_time} - Command: {command}\n')

    def execute_command(command):
        log_command(command)
        subprocess.call(command, shell=True)

    def register_command_logging():
        readline = getattr(__builtins__, 'raw_input', input)
        while True:
            try:
                command = readline('$ ')
                execute_command(command)
            except KeyboardInterrupt:
                break

    register_command_logging()
