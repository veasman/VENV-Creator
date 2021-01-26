# Import os to use mkdir() and other important functions
import os

# Import subprocess to run bash commands later
import subprocess

# Define where the directory is
dir = '/home/vea/Desktop/git/repos/'

# User inputs what the project name will be
projName = input('Enter the name of the project: ')

# Make a directory for the virtual environment and the project
os.mkdir(os.path.join(dir, projName))

# Make a python file inside the project folder
file = open(os.path.join(dir, projName, f'{projName}.py'), 'w')

# Create the venv
os.system('pwd')
os.system('cd ' + os.path.join(dir, projName) + ' && virtualenv venv && source venv/bin/activate')
