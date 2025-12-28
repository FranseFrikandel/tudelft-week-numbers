from ics import Calendar, Event
import datetime

year = 2027

cal = Calendar()

# Get the first monday in September
# TODO: Does academic year always start the monday after 1st september?
day = datetime.date(year, 9, 1)
while day.weekday() != 0:
    day = day + datetime.timedelta(1)

block = 1
week = 1

while block < 5:
    event = Event()
    event.name = f"Week {block}.{week}"
    event.begin = day
    event.end = day + datetime.timedelta(4)
    event.make_all_day()
    cal.events.add(event)
    week += 1
    day = day + datetime.timedelta(7)

    if day.month == 12 and 21 <= day.day <= 27:
        # Chistmas + New years
        day = day + datetime.timedelta(14)

    if week == 11:
        if block == 2:
            # Spring break
            day = day + datetime.timedelta(7)
        block += 1
        week = 1

# For some reason there's 2 newlines everywhere, and thunderbird will
# not read the iCal file if that's the case
output = cal.serialize().replace("\r", "")
print(output)

with open("week_calendar.ics", "w", encoding="utf-8") as f:
    f.write(output)
