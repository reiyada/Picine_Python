import time
import datetime

time_now_utc_in_seconds = time.time()

print("with time:")
print(f"Seconds since January 1, 1970: {time_now_utc_in_seconds} or {time_now_utc_in_seconds:.2e} in scientific notation")


datetime_now_utc_in_seconds = datetime.datetime.now().timestamp()

print("with datetime:")
print(f"Seconds since January 1, 1970: {datetime_now_utc_in_seconds} or {datetime_now_utc_in_seconds:.2e} in scientific notation")