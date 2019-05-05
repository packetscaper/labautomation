#!/usr/bin/env bash

python reset.py edge1 &
python reset.py edge2 &
python reset.py border1 &
python reset.py border2 &


#run cronjob to reset all nodes on Sunday
# crontab -e
#* 5 * * 0 /home/packetscaper/scripts/resetnodes.sh

