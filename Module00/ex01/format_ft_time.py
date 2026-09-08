import time
import datetime

timeNowUtcInSeconds = time.time()

print("with time:")
print(f"Seconds since January 1, 1970: {timeNowUtcInSeconds} or {timeNowUtcInSeconds:.2e} in scientific notation")


dateTimeNowUtcInSeconds = datetime.datetime.now().timestamp()

print("with datetime:")
print(f"Seconds since January 1, 1970: {dateTimeNowUtcInSeconds} or {dateTimeNowUtcInSeconds:.2e} in scientific notation")