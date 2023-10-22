#!/bin/bash

logFile="/var/log/resourceInfoLog.txt"

if [ -f "$logFile" ]; then
    rm "$logFile"
fi

free -m | awk 'NR==2 {printf "%s Memory Usage: %s/%sMB (%.2f%%)\n", strftime("%Y-%m-%d %H:%M:%S"), $3, $2, $3 * 100 / $2 }' >> "$logFile"
df -h | awk '$NF=="/" {printf "%s Disk Usage: %s/%sGB (%s)\n", strftime("%Y-%m-%d %H:%M:%S"), $3, $2, $5 }' >> "$logFile"
uptime | awk '{printf "%s CPU Load: %.2f\n", strftime("%Y-%m-%d %H:%M:%S"), $(NF-2)}' >> "$logFile"
