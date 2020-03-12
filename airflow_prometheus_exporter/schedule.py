from crontab import CronTab

from datetime import datetime
from datetime import timedelta

def get_record_count(current_time, crontab, last_run, last_record_count):

    entry = CronTab(crontab)

    last_scheduled_run = entry.previous(now=current_time)

    last_scheduled_run = current_time + timedelta(seconds=last_scheduled_run)


    delta = last_run - last_scheduled_run
    delta = delta.total_seconds() / (60 * 60)  #differnce in hours

    if delta < 0:
        return -1

    #it ran as expected but more than 24 hours ago
    if ((current_time - last_run).total_seconds() / (60 * 60) > 24):
        return 0

    return last_record_count





#ran normally 1 hour after being scheculed.
rec_count = get_record_count(datetime(2020, 3, 10, 15, 4), '0 7 * * MON-FRI',datetime(2020, 3, 10, 8, 4), 1000)
print(rec_count)


#didn't run
rec_count = get_record_count(datetime(2020, 3, 10, 15, 4), '0 7 * * MON-FRI',datetime(2020, 3, 8, 8, 4), 1000)
print(rec_count)


#it ran fine, but it's the weekend
rec_count = get_record_count(datetime(2020, 3, 15, 15, 4), '0 7 * * MON-FRI',datetime(2020, 3, 13, 8, 4), 1000)
print(rec_count)




