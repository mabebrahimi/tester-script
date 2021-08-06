import os
import sys
import time
import subprocess

DWS_TESTER_COMMAND = os.getenv('DWS_TESTER_COMMAND')
DWS_TESTER_THRESHOLD = os.getenv('DWS_TESTER_THRESHOLD')
DWS_TESTER_INTERVAL = os.getenv('DWS_TESTER_INTERVAL')

i = 0
while i < int(DWS_TESTER_THRESHOLD):
    result = subprocess.run(
        DWS_TESTER_COMMAND.split(), capture_output=True, text=True
    )
    if result.stdout == 0:
        print(0)
        break

    i += 1
    print(f"{i}th-time attempt")
    time.sleep(int(DWS_TESTER_INTERVAL))
else:
    print(1, file=sys.stderr)
