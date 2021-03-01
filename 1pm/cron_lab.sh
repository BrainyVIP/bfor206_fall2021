#!/bin/bash


# use this variable to store the log location for easy re-use
LOG_FILE=~/logs/cron_log.log

echo `date` "cron script is running" >> $LOG_FILE

echo `date` "done." >> $LOG_FILE
