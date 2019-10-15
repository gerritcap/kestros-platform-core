#!/usr/local/bin/python3

from __future__ import print_function
import argparse
import os
import sys
import subprocess
from pathlib import Path

# Configure the command line argument parser
def configure_args_parser():
    args_parser = argparse.ArgumentParser(description='Run git commands across multiple projects.')
    args_parser._action_groups.pop()
    required_args = args_parser.add_argument_group('Required Arguments')
    optional_args = args_parser.add_argument_group('Optional Arguments')
    required_args.add_argument('-c', '--command',
                                action = 'store',
                                dest = 'command',
                                help = '<the command to run>',
                                required = True)
    optional_args.add_argument('--debug',
                                action = 'store_true',
                                dest = 'debug',
                                default = False,
                                help = '<enable verbose args.debugging output>\n')

    return args_parser

# Run an OS command with shell=True
def run_command(command):
    if args.debug:
        print('Running command : {}\n'.format(repr(command)))
    try:
        command_output = subprocess.check_output(command, shell=True)
        return command_output
    except subprocess.CalledProcessError as exception:
        return_code = exception.returncode
        print('Command Failed: {}\n'.format(str(return_code)))
        print(exception.output)
        sys.exit(1)

# The list of git projects to run the command(s) for
git_projects = [
    'slingware-root-project',
    'structured-resource-models',
    'ui-libraries',
    'kestros-structured-assets-core',
    'kestros-structured-images',
    'kestros-cms-foundation',
    'kestros-forms-foundation',
    'kestros-login',
    'kestros-site-administration',
    'kestros-user-management-core',
    'kestros-guides-core',
    'kestros-component-management',
    'kestros-ui-management',
    'kestros-content-objects',
    'kestros-asset-management',
    'kestros-site-management-core',
    'kestros-basic-components',
    'kestros-sample-sites',
    'slingware-site',
    'slingware-devops']

# Process the command line arguments and run the git command(s) for each project
try:
    args_parser = configure_args_parser()
    args = args_parser.parse_args()

    print('\nRunning \"{}\" with git helper. . .'.format(args.command))

    # Check for the args.debug flag and print out the command line args
    if args.debug:
        print('\n{}'.format(str(sys.argv)))

    # Figure out the current working directory
    base_directory = os.path.dirname(os.path.realpath(sys.argv[1]))
    if args.debug:
        print('\nWorking directory: {}\n'.format(base_directory))

    # Get the path for one directory level up
    project_directory = Path(base_directory).parents[0]
    if args.debug:
        print('\nProject directory: {}\n'.format(project_directory))

    # Loop through the repositories
    for project in git_projects:
        # Check if we're doing a clone and cd to the correct directory level
        if 'git clone' in args.command:
            os.chdir('{}'.format(project_directory))
            print(run_command('{} {}'.format(args.command, 'git@github.com:slingware/')))
        print('Running \"{}\" in {}'.format(args.command, project))
        os.chdir('{}/{}'.format(project_directory, project))
        print(run_command(args.command).decode('ascii'))

except Exception as error_message:
    print(error_message)
    sys.exit(1)
except IOError as error_message:
    args_parser.error(str(error_message))






