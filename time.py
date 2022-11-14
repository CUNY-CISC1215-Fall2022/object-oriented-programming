# In this file, we use classes to model a duration of time:
class Time:
    pass

# Print out a Time object
def print_time(t):
    print(str(t.hour) + ":" + str(t.minute) + ":" + str(t.second))

# Convert a Time object to a number of seconds
def time_to_seconds(t):
    seconds = t.hour * 60 * 60
    seconds += t.minute * 60
    seconds += t.second

    return seconds

# Convert a number of seconds to a new Time object
def seconds_to_time(seconds):
    t = Time()
    t.second = seconds
    t.minute = 0
    t.hour = 0

    if t.second >= 60:
        t.minute += t.second // 60
        t.second = t.second % 60

    if t.minute >= 60:
        t.hour += t.minute // 60
        t.minute = t.minute % 60
    
    return t

# Add two time objects together. Returns a new Time object
# containing the sum of both.
def add_time(t1, t2):
    s1 = time_to_seconds(t1)
    s2 = time_to_seconds(t2)
    return seconds_to_time(s1 + s2)

# Destructively increment the given Time object by the given number
# of seconds
def increment(t, duration):
    s = time_to_seconds(t)
    s = s + duration

    t2 = seconds_to_time(s)
    t.second = t2.second
    t.minute = t2.minute
    t.hour = t2.hour




time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30

print_time(time1)
increment(time1, 31)
print_time(time1)