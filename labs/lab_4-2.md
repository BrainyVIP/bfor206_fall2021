# BFOR 206 Lab
## Class 4-2: read/write


# Task Description

Write a script that pings a website
and logs the date/time and the ping
result to a log file.



# Normal Scenario

## Input
**File:** File containing a URL or IP address

## Output
**File:** The date/time and output of the ping
          ping command.





# Test Cases

```shell
######## Normal scenarios ##########

# Input (from file):
google.com

# Output (in a file)

Script Started at Tue Feb 23 18:30:59 PST 2021

PING google.com (142.250.69.206): 56 data bytes
64 bytes from 142.250.69.206: icmp_seq=0 ttl=118 time=20.512 ms
64 bytes from 142.250.69.206: icmp_seq=1 ttl=118 time=27.849 ms
64 bytes from 142.250.69.206: icmp_seq=2 ttl=118 time=27.540 ms

--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 20.512/25.300/27.849/3.388 ms

Done.

Script Started at Tue Feb 23 18:40:00 PST 2021

PING google.com (142.250.69.206): 56 data bytes
64 bytes from 142.250.69.206: icmp_seq=0 ttl=118 time=20.512 ms
64 bytes from 142.250.69.206: icmp_seq=1 ttl=118 time=27.849 ms
64 bytes from 142.250.69.206: icmp_seq=2 ttl=118 time=27.540 ms

--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 20.512/25.300/27.849/3.388 ms

Done.
```




# Submission instructions

**Scripts that output bash errors will not be accepted!**

Run the script at least twice to show the
results being appendend to the file.

When you are finished, submit two screenshots on Blackboard:
1.  A screenshot of your code.
2.  A screenshot of the output file that looks very
    similar to the output in the test cases.
