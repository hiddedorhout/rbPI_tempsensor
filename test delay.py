import sched, time, datetime

# Write to db schedule
s = sched.scheduler(time.time, time.sleep)


def write_data(sc):
    logtime = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    value = "Hallo!"
    print(value, logtime)
    sc.enter(5, 1, write_data, (sc,))

s.enter(0, 5, write_data, (s,))
s.run()