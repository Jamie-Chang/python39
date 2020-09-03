# IANA database by default
# Windows does not ship IANA, $ pip install tzinfo

from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

# Daylight saving time
dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
assert str(dt) == "2020-10-31 12:00:00-07:00"
assert dt.tzname() == 'PDT'

# Standard time
dt += timedelta(days=7)
assert str(dt) == "2020-11-07 12:00:00-08:00"
assert dt.tzname() == 'PST'


# side-note, not introduced here but useful

duration = timedelta(weeks=1)
print(f"{duration / timedelta(days=1)} days in a week")
print(f"{duration / timedelta(hours=1)} hours in a week")
print(f"{duration / timedelta(minutes=1)} minutes in a week")
print(f"{duration / timedelta(seconds=1)} seconds in a week")
