#!/bin/bash

# file to log the scripts output.
LOG_FILE=~/logs/cronlog.log

echo `date` "cron script is running." >> $LOG_FILE

echo `date` "done." >> $LOG_FILE
