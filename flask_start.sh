#!/bin/bash

NAME="Flask Loto Scraper"                              #Name of the application (*)
USER=root                                        # the user to run as (*)
GROUP=root                                     # the group to run as (*)
echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd /root/lotoScraper
source /root/flask_venv/bin/activate

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec python flaskApp.py

