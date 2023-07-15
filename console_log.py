import os
import subprocess

log_file = 'command_log.txt'

def console_log():

    def log_command(command):
        with open(log_file, 'a') as file:
            file.write(f'Command: {command}\n')

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
