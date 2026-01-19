time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_for_work = time.replace(',', ' ').split()

minutes = 0

for t in time_for_work:
    if 'h' in t:
        minutes += int(t.replace('h', ''))*60
    elif 'm' in t:
        minutes += int(t.replace('m', ''))
    else:
        minutes += int(t.replace('s', ''))//60

print(minutes)







