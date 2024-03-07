#!/bin/bash

crontab -l > newcron

echo "0 6 * * * /usr/bin/python3 scrape.py" >> newcron

crontab newcron
rm newcron