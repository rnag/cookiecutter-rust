"""
Does the following:

1. Removes main.rs if not a service project
2. Configures CI if requested
3. Initializes git
"""
from __future__ import print_function
import os
import shutil
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)


def remove_dir(filename):
    """
    generic remove folder (directory) from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        shutil.rmtree(fullpath)


def init_git():
    """
    Initializes git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


# remove service specific files if we're writing a library
if '{{ cookiecutter.project_type }}'.lower() == 'library':
    remove_file('src/main.rs')
    
# 4. Remove unused ci choice
if '{{ cookiecutter.use_ci}}'.lower() != 'github':
    remove_dir(".github")

# 5. Initialize Git (should be run after all file have been modified or deleted)
init_git()
